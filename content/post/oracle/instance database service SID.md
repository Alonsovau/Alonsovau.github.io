---
author: "Xin Zhou"
date: 2017-03-31
linktitle: instance database service SID
title: instance database service SID
weight: 10
tags: [
    "oracle"
]
categories: [
    "Oracle"
]
---
A database instance is a set of memory structures that manage database files. A database is a set of physical files on disk created by the CREATE DATABASE statement. The instance manages its associated data and serves the users of the database.

Every running Oracle database is associated with at least one Oracle database instance. Because an instance exists in memory and a database exists on disk, an instance can exist without a database and a database can exist without an instance.

#### Database Instance Structure

When an instance is started, Oracle Database allocates a memory area called the system global area (SGA) and starts one or more background processes. The SGA serves various purposes, including the following:

- Maintaining internal data structures that are accessed by many processes and threads concurrently

- Caching data blocks read from disk

- Buffering redo data before writing it to the online redo log files

- Storing SQL execution plans

The SGA is shared by the Oracle processes, which include server processes and background processes, running on a single computer. The way in which Oracle processes are associated with the SGA varies according to operating system.

A database instance includes background processes. Server processes, and the process memory allocated in these processes, also exist in the instance. The instance continues to function when server processes terminate.

![image](https://docs.oracle.com/cd/E11882_01/server.112/e40540/img/cncpt325.gif)

#### Database Instance Configurations

You can run Oracle Database in either of the following mutually exclusive configurations:

- Single-instance configuration：

A one-to-one relationship exists between the database and an instance.

- Oracle Real Application Clusters (Oracle RAC) configuration：

A one-to-many relationship exists between the database and instances.

![image](https://docs.oracle.com/cd/E11882_01/server.112/e40540/img/cncpt296.gif)

##### Oracle System Identifier (SID)

The system identifier (SID) is a unique name for an Oracle database instance on a specific host. On UNIX and Linux, Oracle Database uses the SID and Oracle home values to create a key to shared memory. Also, the SID is used by default to locate the parameter file, which is used to locate relevant files such as the database control files.

On most platforms, the ORACLE\_SID environment variable sets the SID, whereas the ORACLE\_HOME variable sets the Oracle home. When connecting to an instance, clients can specify the SID in an Oracle Net connection or use a net service name. Oracle Database converts a service name into an ORACLE\_HOME and ORACLE_SID.
