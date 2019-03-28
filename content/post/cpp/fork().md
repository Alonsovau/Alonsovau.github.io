---
author: "Xin Zhou"
date: 2019-02-28
linktitle: fork()
title: fork()
weight: 10
tags: [
    "linux", "cpp"
]
categories: [
    "CPP"
]
---

```cpp

#include <stdio.h>

#include <stdlib.h>

#include <unistd.h>

#include <set>

#include <sys/wait.h>



using namespace std;



int main(int argc, char const *argv[])

{

    int num = 5;

    set<int> pid_set;

    int seq = 0;

    pid_t temp_pid;



    for (int i=0; i < num; i++)

    {

        temp_pid = fork();

        if (temp_pid ==0 || temp_pid == -1)

            break;



        pid_set.insert(temp_pid);

        seq++;

    }



    if (temp_pid == 0)

    {

        for (int j=0; j < 10; j++)

        {

            printf("%d---%d---%d\n", getpid(), j, seq);

            if (seq == 0)

            {

                char *p = NULL;

                printf("%c", *p);

            }

            sleep(seq);

        }

        return 0;

    }



    else

    {

        int stat = 0;

        int ret = 0;



        while(true){

            ret = waitpid(0, &stat, WNOHANG);

            if (ret > 0)

            {

                set<int>::iterator position = pid_set.find(ret);

                if (position != pid_set.end())

                    pid_set.erase(position);

                if (WIFSIGNALED(stat))

                    printf("term %d, %d\n", ret, WTERMSIG(stat));

                if (WIFEXITED(stat))

                    printf("exit %d, %d\n", ret, WEXITSTATUS(stat));

            }



            if (pid_set.size() == 0)

            {

                exit(0);

            }

        }



    }





    return 0;

}

```
