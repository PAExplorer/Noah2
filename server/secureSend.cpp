#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <string.h>

#define PORT 12345

int main(int argc, char **argv) {
    // Create a socket.
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Failed to create socket");
        return -1;
    }

    // Set the socket options.
    int enable = 1;
    if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &enable, sizeof(enable)) < 0) {
        perror("Failed to set socket options");
        return -1;
    }

    // Bind the socket to a local address.
    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = htonl(INADDR_ANY);
    addr.sin_port = htons(PORT);
    if (bind(sockfd, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("Failed to bind socket");
        return -1;
    }

    // Listen for incoming connections.
    if (listen(sockfd, 1) < 0) {
        perror("Failed to listen for connections");
        return -1;
    }
        // Authenticate the connection with a password.
    char password[1024];
    printf("Password: ");
    fgets(password, 1024, stdin);
    if (strcmp(password, "mypassword\n") != 0) {
        printf("Invalid password\n");
        close(connfd);
        continue;
    }

    // Read the file to send.
    FILE *file = fopen(argv[1], "rb");
    if (!file) {
        perror("Failed to open file");
        close(connfd);
        continue;
    }

    // Send the file over the network.
    char buffer[1024];
    int bytes_read;
    while ((bytes_read = fread(buffer, 1, sizeof(buffer), file)) > 0) {
        int bytes_sent = send(connfd, buffer, bytes_read, 0);
        if (bytes_sent < 0) {
            perror("Failed to send file");
            break;
        }
    }

    // Close the file and the connection.
    fclose(file);
    close(connfd);
}

return 0;