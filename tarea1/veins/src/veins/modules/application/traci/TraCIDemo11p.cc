//
// Copyright (C) 2006-2011 Christoph Sommer <christoph.sommer@uibk.ac.at>
//
// Documentation for these modules is at http://veins.car2x.org/
//
// SPDX-License-Identifier: GPL-2.0-or-later
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//

#include "veins/modules/application/traci/TraCIDemo11p.h"
#include "veins/modules/application/traci/TraCIDemo11pMessage_m.h"
#include <string>

using namespace veins;

Define_Module(veins::TraCIDemo11p);

void TraCIDemo11p::initialize(int stage)
{
    DemoBaseApplLayer::initialize(stage);
    if (stage == 0) {
        sentMessage = false;
        lastDroveAt = simTime();
        currentSubscribedServiceId = -1;
    }
}

void TraCIDemo11p::onWSA(DemoServiceAdvertisment* wsa)
{
    if (currentSubscribedServiceId == -1) {
        mac->changeServiceChannel(static_cast<Channel>(wsa->getTargetChannel()));
        currentSubscribedServiceId = wsa->getPsid();
        if (currentOfferedServiceId != wsa->getPsid()) {
            stopService();
            startService(static_cast<Channel>(wsa->getTargetChannel()), wsa->getPsid(), "Mirrored Traffic Service");
        }
    }
}



//(PROGRAMAMOS EL CAMBIO DE RUTA EN UN TIEMPO FUTURO)
void TraCIDemo11p::onWSM(BaseFrame1609_4* frame) {
    // Variable estática para llevar un registro de cuántas veces se ha ejecutado una acción específica.
    static int actionCount = 0;

    TraCIDemo11pMessage* wsm = check_and_cast<TraCIDemo11pMessage*>(frame);

    // Variables para el ID de movilidad y para saber si se debe reenrutar.
    int nodeId = mobility->getId();

    // Cambia la ruta del vehículo si es el nodo objetivo y no ha ejecutado la acción antes.

    if (wsm->getReroute() && nodeId == 35 && actionCount == 0) {
        std::string destinationRoadId = wsm->getDestinationRoadId();
        findHost()->getDisplayString().setTagArg("i", 1, "green");
        traciVehicle->changeRoute(destinationRoadId.c_str(), 9999);
        std::cout << "CAMBIA RUTA" << std::endl;
        actionCount++;
        }

    if (!sentMessage && actionCount == 0 && wsm->getServicio()) {
        sentMessage = true;
        wsm->setSenderAddress(myId);
        wsm->setSerial(1);
        scheduleAt(simTime() + uniform(2.01, 2.2), wsm->dup());
    }
}



// Maneja los mensajes automáticos en una simulación de red vehicular.
void TraCIDemo11p::handleSelfMsg(cMessage* msg) {
    // Intenta convertir el mensaje entrante a un tipo específico utilizado en este contexto de simulación.
    TraCIDemo11pMessage* wsm = dynamic_cast<TraCIDemo11pMessage*>(msg);

    // Si el mensaje no es del tipo esperado, pásalo al manejador de la clase base y retorna.
    if (!wsm) {
        DemoBaseApplLayer::handleSelfMsg(msg);
        return;
    }

    // Recupera el número de serie del mensaje.
    int messageSerial = wsm->getSerial();
    // Recupera el ID del modelo de movilidad asociado con este nodo.
    int nodeId = mobility->getId();

    // Si el número de serie del mensaje es 2, establece el indicador de reenrutamiento a verdadero y muestra un mensaje.
    if (messageSerial == 3) {
        wsm->setReroute(true);
        wsm->setFwd(wsm->getReroute());
    }

    // Si el ID del nodo no es 17, registra el ID y reenvía el mensaje.
    if (nodeId != 17) {
        sendDown(wsm->dup());
    }

    // Incrementa el número de serie del mensaje y actualiza el mensaje.
    messageSerial++;
    wsm->setSerial(messageSerial);
    wsm->setFwdno(wsm->getSerial());
    // Si el número de serie actualizado es 3 o mayor, termina el servicio y elimina el mensaje.
    if (messageSerial >= 4) {
        stopService();
        delete wsm;
    } else {
        // De lo contrario, programa este mensaje para ser enviado nuevamente después de 5 unidades de tiempo de simulación.
        scheduleAt(simTime() + 2, wsm);
    }
}

// Maneja las actualizaciones de posición en una simulación de red vehicular.
void TraCIDemo11p::handlePositionUpdate(cObject* obj) {
    // Llama al método de la clase base para el manejo básico de la actualización de posición.
    DemoBaseApplLayer::handlePositionUpdate(obj);


    static bool hasUpdated = false;  // Flag para controlar la actualización única.
    const int targetVehicleId = 17;  // ID del vehículo monitoreado.
    int currentVehicleId = mobility->getId();  // Obtiene el ID del vehículo actual.

    // Solo maneja la lógica específica para el vehículo monitoreado y si aún no se ha actualizado.
    if (currentVehicleId == targetVehicleId && !hasUpdated) {

        if (simTime() - lastDroveAt >= 5) {
            // Cambia el icono del host a rojo para indicar una acción.
            findHost()->getDisplayString().setTagArg("i", 1, "red");

            // Crea y configura un nuevo mensaje.
            TraCIDemo11pMessage* wsm = new TraCIDemo11pMessage();
            populateWSM(wsm);
            //ENVIAMOS MENSAJES DE LA RUTA DESTINO, DEL SERVICIO Y VELOCIDAD
            wsm->setSpeed(mobility->getVehicleCommandInterface()->getSpeed());
            wsm->setDestinationRoadId("400008031#3");
            wsm->setServicio(true);
            // Envía el mensaje dependiendo de si los datos están en el canal de servicio.
            if (dataOnSch) {
                startService(Channel::sch2, 42, "Traffic Information Service");
                scheduleAt(computeAsynchronousSendingTime(1, ChannelType::service), wsm);
            } else {
                sendDown(wsm);
            }

            // Marca que se ha realizado la actualización.
            hasUpdated = true;
        }
    } else if (currentVehicleId != targetVehicleId) {
        lastDroveAt = simTime();
    }
}




