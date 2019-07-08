#include <stdio.h>
#include <winsock2.h>     /* for all WinSock functions */
#define MAXPENDING 5    /* Max outstanding connection requests */
#define RCVBUFSIZE 256  /* Size of receive buffer */
#define ERR_EXIT { \
    fprintf(stderr, "ERROR: %ld\n", WSAGetLastError()); \
    WSACleanup();  return 0; }
    int main(int argc, char *argv[]) { WSADATA wsaData;
    SOCKET rv_sock, s_sock;
    int port_num, msg_len;
    char buffer[RCVBUFSIZE]; struct sockaddr_in serv_addr;
        if (argc != 2) {  /* Test for correct number of arguments */
            fprintf(stdout, "Usage: %s server_port\n", argv[0]);
    return 0; }
        WSAStartup(MAKEWORD(2,2), &wsaData);/* Initialize Winsock */
    rv_sock = WSASocket(PF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, 0, WSA_FLAG_OVERLAPPED);
    if (rv_sock == INVALID_SOCKET) ERR_EXIT;
    memset((char *) &serv_addr, 0, sizeof(serv_addr));
    port_num = atoi(argv[1]); /* First arg: server port num. */ serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1"); serv_addr.sin_port = htons(port_num);
    if (bind(rv_sock, (SOCKADDR*) &serv_addr,
    sizeof(serv_addr)) == SOCKET_ERROR) { closesocket(rv_sock);
    ERR_EXIT;
    }
    if (listen(rv_sock, MAXPENDING) == SOCKET_ERROR) {
    closesocket(rv_sock);
    ERR_EXIT; }
    while ( 1 ) { /* Server runs forever */ fprintf(stdout, "\nWaiting for client to connect...\n"); if (s_sock = accept(rv_sock, NULL, NULL)
    == INVALID_SOCKET) ERR_EXIT;
    memset(buffer, 0, RCVBUFSIZE);
    msg_len = recv(s_sock, buffer, RCVBUFSIZE - 1, 0); if (msg_len == SOCKET_ERROR) ERR_EXIT; fprintf(stdout, "Client's message: %s\n", buffer); msg_len = send(s_sock, "I got your message", 18, 0); if (msg_len == SOCKET_ERROR) ERR_EXIT; closesocket(s_sock);
    }
    return 0; }