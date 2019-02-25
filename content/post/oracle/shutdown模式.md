---
author: "Xin Zhou"
date: 2017-03-31
linktitle: shutdown模式
title: shutdown模式
weight: 10
tags: [
    "oracle"
]
categories: [
    "Oracle"
]
---
- SHUTDOWN ABORT

    This mode is intended for emergency situations, such as when no other form of shutdown is successful. This mode of shutdown is the fastest. However, a subsequent open of this database may take substantially longer because instance recovery must be performed to make the data files consistent.

- SHUTDOWN IMMEDIATE

    This mode is typically the fastest next to SHUTDOWN ABORT. Oracle Database terminates any executing SQL statements and disconnects users. Active transactions are terminated and uncommitted changes are rolled back.

- SHUTDOWN TRANSACTIONAL

    This mode prevents users from starting new transactions, but waits for all current transactions to complete before shutting down. This mode can take a significant amount of time depending on the nature of the current transactions.

- SHUTDOWN NORMAL

    This is the default mode of shutdown. The database waits for all connected users to disconnect before shutting down.
