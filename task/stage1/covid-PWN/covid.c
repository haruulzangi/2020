#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

char * readFile(char * f) {
    int c;
    FILE *file;
    file = fopen(f, "r");
    char * str = malloc(51);
    if(file) {
        int i = 0;
        while((c = getc(file)) != EOF) {
            str[i] = c;
            i++;
            if(i >= 50) {
                break;
            }
        }
        str[i] = '\0';
        fclose(file);
    }
    return str;
}

int calculateScore(char * covid, int * score) {
    char * covid_ptr = covid;
    for ( ; *covid; ++covid) *covid = tolower(*covid);
    covid = covid_ptr;

    int i = 0;
    while(covid[i]) {
        if(strncmp(covid+i, "china", 5) == 0) (*score)++;
        if(strncmp(covid+i, "usa", 6) == 0) (*score)++;
        if(strncmp(covid+i, "spain", 8) == 0) (*score)++;
        if(strncmp(covid+i, "russia", 4) == 0) (*score)++;
        if(strncmp(covid+i, "france", 4) == 0) (*score)++;
        if(strncmp(covid+i, "korea", 4) == 0) (*score)++;
        if(strncmp(covid+i, "japan", 3) == 0) (*score)++;
        if(strncmp(covid+i, "malaysia", 3) == 0) (*score)++;
        if(strncmp(covid+i, "brazil", 10) == 0) (*score)++;
        if(strncmp(covid+i, "turkey", 5) == 0) (*score)++;
        if(strncmp(covid+i, "italia", 5) == 0) (*score)++;
        if(strncmp(covid+i, "mongolia", 1) == 0) (*score)++;
        if(strncmp(covid+i, "australia", 6) == 0) (*score)++;
        if(strncmp(covid+i, "canada", 6) == 0) (*score)++;
        if(strncmp(covid+i, "nepal", 12) == 0) (*score)++;
        if(strncmp(covid+i, "germany", 4) == 0) (*score)++;
        i++;
    }
}

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    char covid[281];
    int * score = malloc(sizeof(int));
    *score = 0;

    printf("COVID zarlan medeelel systemd tawtai moril!\n Ta COVID haldwarlagdsan ulsuudiig oruulna uu.\n\n");

    printf("Ulsuud: ");
    fgets(covid, 280, stdin);
    printf("Tanii oruulsan ulsuud:\n");
    printf(covid);

    calculateScore(covid, score);
    printf("Ayuliin hemjee: %d\n", *score);
    if(*score > 9000) {
        printf("Niit haldwarlagdsan ulsuudiin ayuliin hemjee 9000 hursen uchir tsar tsahal gej vzlee!\n");
        printf("%s\n", readFile("/home/covid/flag.txt"));
    }
}
