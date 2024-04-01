#!/usr/bin/expect -f

# Verificar el número correcto de argumentos
if {[llength $argv] != 4} {
    puts "Uso: $argv0 <username> <password> <host> <comando>"
    exit 1
}

# Obtener los argumentos de la línea de comandos
set username [lindex $argv 0]
set password [lindex $argv 1]
set host [lindex $argv 2]
set comando [lindex $argv 3]

# Comando plink para conectar mediante SSH
spawn plink -ssh -l $username -pw $password $host

# Esperar a que aparezca la pregunta sobre continuar con la conexión
expect {
    "Continue with connection? (y/n)" {
        send "y\r"
        exp_continue
    }
    "Further authentication required" {
        send "\r"
        exp_continue
    }
    "Access granted. Press Return to begin session." {
        send "\r"
        exp_continue
    }
    ">" {
        send "enable\r"
        exp_continue
    }
    "#" {
        # Enviar el comando arbitrario ingresado como parámetro
        send "$comando\r"
        expect -re ".+"
        # Mandar un enter
        send "\r"
    }
}

# Cerrar el proceso
close

