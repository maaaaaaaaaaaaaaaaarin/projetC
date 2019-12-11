
all: client, serveur, proxy

client: clean
	@gcc client.c -o ./client
	@chmod 755 ./client
	@#./client

serveur: clean
	@gcc serveur.c -o ./serveur
	@chmod 755 ./serveur
	@#./serveur

proxy: clean
	@gcc proxy.c -o ./proxy
	@chmod 755 ./proxy
	@#./proxy

clean:
	@rm -f serveur client
	@clear
	@echo "Clean completed"
