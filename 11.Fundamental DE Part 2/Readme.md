## Rangkuman Fundamental DE Part 2

### What is Structured Data?
-Structured data is data that has a defined data model, format and schema, such as: field such as name, address, zip code. It is stored in relational database (RDBMS) and easily searched through SQL.
-Estimated 20% of enterprise data
-Requires less storage

### What is Unstructured Data?
-Unstructured data is data that has internal structure but is not structured via pre-defined data models of schemas. Unstructured data does not fit nicely into relational database like SQL and need advanced processing to make it searchable.
-Example:
    - Text documents, pdfs, images, videos
    - Social media: data from twitter, facebook, instagram
-Estimated 80% of enterprise data
-Requires more storage

### What is Semi-structured Data?
-The semi-sturctured data, however, falls somewhere between structured and unstructured.
-Semi-structured data does not have a rigid schema, so it does not conform to a data table or relational database structure. However, it has classifying characteristics associated with it, such as metadata that enable analysis. Metadata asscociated with unstructured data.

### Relational Database
-A relational database is a collection of data items with pre-defined relationships between them.

### Database Normalization
-Database normalization is a database principle for organizing data in an organized and consistent way.
-The main purpose of database normalization is to avoid complexities, eliminate duplicates, maintain the integrity of the database and organize data in a consistent way. In normalization, the data is divided into several tables linked together with relationships.
-It also helps you eliminate undesirable characteristics associated with insertion, deletion, and updating.

### NoSQL Database
-NoSQL databases supports more semi-structured data and have flexible schemas for building modern applications.
-NoSQL databases are typically distributed systems where several machines work together in clusters.

### NoSQL: Key-Value DB
-A database that stores data as a collection of key-value pairs in in-memory/RAM storage.
-In-memory data stores don't require a trip to disk, that enables low latency and high throughput data access.
-The key serves as a unique identifier (hashed)
-The values can be scalar data types (integer, string), JSON, array, etc.

### Key-Value DB Use Cases
-Use Case:
    - Caching Key-value DB can improve the read performance of an application
    - User session management. Key-value DB can efficiently store and retrieve user info, such as: auth-token, user preferences, personalized data and themes, recommendations, etc.
    - Gaming leaderboards. Key-value DB can be used to store and retrieve high scores and rangkings for online games.
-Tools:
    - Redis
    - Memcached
    - Riak

### NoSQL: Wide-Column DB
-A type NoSQL database that stores data in a column-family format within a distributed system architecture.
-It uses tables, rows, and columns, but unlike relational database, the names and format of the columns can vary from row to row in the same table.

### NoSQL: Graph DB
-A graph DB stores nodes and edge instead of tables, or documents.
-There are no JOINs or lookups. Relationships are stored natively alogside the nodes.
-Graph data modeling :
    https://www.google.com/url?q=https://neo4j.com/developer/data-modeling/&sa=D&source=editors&ust=1711215146990377&usg=AOvVaw24lDirWAvFzSu2xkpzAH-W

### OLTP vs OLAP
-Types of database based on the purpose of the query : OLTP and OLAP
-RDBMS is good to maintain OLTP use cases. OLTP is a data processing category that deals with numerous transactions performed by many users that involve inserting, updating, and deleting data.
-Data Warehouse is good to maintain OLAP use cases: to answer multi-dimensional analytical queries.

### DATA MART
-A data mart is a subset of a data warehouse focused on a particular line of business, department, or subject area.
-Data marts make specific data available to a defined group of users, which allows those users to quickly access critical insights without wasting time searching through an entire data warehouse.
-For example, many companies may have a data mart that aligns with a specific department in the business, such as finance, sales, or marketing.