#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h> /* socket(), bind(), listen(), accept(), recv(), send(), htonl(), htons() */
/* perror(), fprintf(), sprintf() */
/* for atoi() */
/* for memset() */
                          
#include <arpa/inet.h>  /* for sockaddr_in */
#include <unistd.h>     /* for close() */
#define MAXPENDING 5    /* Max outstanding connection requests */
#define RCVBUFSIZE 256  /* Size of receive buffer */
#define ERR_EXIT(msg) { perror(msg); exit(1); }

int main(int argc, char *argv[]) {
int rv_sock, s_sock, port_num, msg_len; char buffer[RCVBUFSIZE];
struct sockaddr_in serv_addr;
    if (argc != 2) {  /* Test for correct number of arguments */
        char msg[64];  memset((char *) &msg, 0, 64);
        sprintf(msg, "Usage: %s server_port\n", argv[0]);
        ERR_EXIT(msg);
    }
    rv_sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (rv_sock < 0) ERR_EXIT("ERROR opening socket"); memset((char *) &serv_addr, 0, sizeof(serv_addr));
    port_num = atoi(argv[1]); /* First arg: server port num. */ serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY); serv_addr.sin_port = htons(port_num);
    if (bind(rv_sock,
    (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
    ERR_EXIT("ERROR on binding"); if (listen(rv_sock, MAXPENDING) < 0)
            ERR_EXIT("ERROR on listen");
    while ( 1 ) { /* Server runs forever */ fprintf(stdout, "\nWaiting for client to connect...\n"); s_sock = accept(rv_sock, NULL, NULL);
    if (s_sock < 0) ERR_EXIT("ERROR on accept new client"); memset(buffer, 0, RCVBUFSIZE);
    msg_len = recv(s_sock, buffer, RCVBUFSIZE - 1, 0); if (msg_len < 0)
                ERR_EXIT("ERROR reading from socket");
            fprintf(stdout, "Client's message: %s\n", buffer);

    msg_len = send(s_sock, "I got your message", 18, 0); if (msg_len < 0) ERR_EXIT("ERROR writing to socket"); close(s_sock);
        }
        /* NOT REACHED, because the server runs forever */
}