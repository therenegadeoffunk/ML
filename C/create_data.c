#include <stdio.h>
#include <sqlite3.h>

int main(int argc, char* argv[])
{
    sqlite3 *conn;
    sqlite3_open("music.db", &conn);
    char *query;
    char *err;
    query = "INSERT INTO songs VALUES ( 2, 'fun song', 120, 'silly artist', 'rock', 35, 8, 1 )";
    sqlite3_exec(conn, query, 0, 0, &err);
    sqlite3_close(conn);
    return 0;
}
