#include <stdio.h> /* for perror(), fprintf(), sprintf() */
#include <stdlib.h> /* for atoi() */
#include <string.h> /* for memset(), memcpy(), strlen() */
#include <sys/socket.h> /* for sockaddr, socket(), connect(),  recv(), send(), htonl(), htons() */
#include <arpa/inet.h>  /* for sockaddr_in */
#include <netdb.h>      /* for hostent, gethostbyname() */
#include <unistd.h>     /* for close() */
#define RECVBUFSIZE 256 /* Size of receive buffer */
#define ERR_EXIT(msg) { perror(msg); exit(1); }
int main(int argc, char *argv[]) { 
    int c_sock, port_num, msg_len; 
    struct sockaddr_in serv_addr; 
    struct hostent *serverIP; 
    char buffer[RECVBUFSIZE];
    if (argc != 3) {   /* Test for correct number of arguments */
        char msg[64];  memset((char *) &msg, 0, 64);  /* erase */
        sprintf(msg, "Usage: %s serv_name serv_port\n", argv[0]);
        ERR_EXIT(msg);
    }
    serverIP = gethostbyname(argv[1]); /* 1st arg: server name */
    if (serverIP == NULL)
        ERR_EXIT("ERROR, server host name unknown");
    //printf("id%s",argv[1]);


    port_num = atoi(argv[2]); /* Second arg: server port num. */ 
    c_sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (c_sock < 0) ERR_EXIT("ERROR opening socket"); 
    char str[32];
    printf("%s\n",inet_ntop(serverIP->h_addrtype,serverIP->h_addr,str,sizeof(str)));
    printf("%d\n",serverIP->h_length);
    //char * h;
    //scanf("input",h);
    memset((char *) &serv_addr, 0, sizeof(serv_addr)); 
    serv_addr.sin_family = AF_INET;
    memcpy((char *) &serv_addr.sin_addr.s_addr,(char *) &(serverIP->h_addr), serverIP->h_length); 
    serv_addr.sin_port = htons(port_num);
    if (connect(c_sock,(struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) ERR_EXIT("ERROR connecting");
    fprintf(stdout, "User, enter your message: "); 
    memset(buffer, 0, RECVBUFSIZE); /* erase */
    fgets(buffer, RECVBUFSIZE, stdin); /* read input */ 
    msg_len = send(c_sock, buffer, strlen(buffer), 0); 
    if (msg_len < 0) ERR_EXIT("ERROR writing to socket"); 
    memset(buffer, 0, RECVBUFSIZE);
    msg_len = recv(c_sock, buffer, RECVBUFSIZE - 1, 0);
    if (msg_len < 0) ERR_EXIT("ERROR reading from socket"); fprintf(stdout, "Server says: %s\n", buffer); close(c_sock);
    exit(0);
}