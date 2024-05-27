# Nome: Tommaso Valeriani
# Matricola: 0001081795
# Monitoraggio di rete

from pythonping import ping
import time

def gestione_scelta(scelta, hosts):
    if scelta == 'n':
        print("\nHai scelto di inserire nuovi host da monitorare")
        nuovi_hosts = input("\nInserire uno o più host che si desidera monitorare, separati da spazi: ").split()
        hosts.extend(nuovi_hosts) # aggiungo i nuovi host a tutti gli altri
        return hosts
    elif scelta == 'q':
        print("\nInterruzione del monitoraggio in corso...")
        return None
    else:
        print("Scelta non valida, riprovare")
        return hosts

def is_host_online(host):
    # La funzione esegue un ping per verificare se il relativo host fornito in input sia online,
    # restituendo un booleano
    try:
        # Timeout stabilito al fine di considerare ogni host che non risponde entro tale tempo offline
        risposta = ping(host, count=1, timeout=1)
        return risposta.success()
    # Gestione dell'eventuale errore restituito in caso di un ping fallito
    except Exception as e:
        print(f"Errore nel ping a {host}: {e}")
        return False

def controllo_hosts(hosts):
    # La funzione controlla lo stato della lista degli host forniti in input, restituendo
    # come output un dizionario contenente come chiavi gli host, e come valori il loro stato
    stato = {}
    for host in hosts:
        stato[host] = "online" if is_host_online(host) else "offline"
    return stato

def main():
    # La funzione main legge gli host forniti in input dall'utente e ne restituisce lo stato
    hosts = input("\n\nInserire uno o più host che si desidera monitorare, separati da spazi: ").split()
    
    while True: # Gestisco la possibilità di poter inserire host nuovi dopo quelli iniziali,
                # che verranno inseriti estendendo la lista di host iniziale in modo da ricontrollarne lo stato
        stato = controllo_hosts(hosts)
        # Per ogni host il programma stampa se sia online oppure offline
        for host, state in stato.items():
            print(f"\n{host} è {state}")
            time.sleep(2) # Sleep inserito per una migliore leggibilità del terminale
        
        # Gestione delle differenti scelte che l'utente può intraprendere
        print("\nPremere 'n' se si desidera inserire nuovi host da monitorare \nPremere 'q' se si desidera uscire dal programma")
        scelta = input("Selezionare una operazione da eseguire: ")
        hosts = gestione_scelta(scelta, hosts)
        if scelta == 'q' or hosts is None:
            time.sleep(2) # Sleep inserito per una migliore leggibilità del terminale
            break
        
if __name__ == "__main__":
    main()