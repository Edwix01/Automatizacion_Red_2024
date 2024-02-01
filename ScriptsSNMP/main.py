import des_int
import des_disp
import p_tab

ba = input("Ingrese la barra de direcciones a analizar Ejm:(192.168.10.1): ")
disp = des_disp.dis_act(ba,1,6)
i_act = des_int.in_act(disp)


p_tab.display_interface_table(i_act)