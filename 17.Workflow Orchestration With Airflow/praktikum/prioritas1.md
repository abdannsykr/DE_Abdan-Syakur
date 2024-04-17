Nomer 1
    a. Satu task menggambarkan perintah bash yang harus dijalankan.
    b. Gunakan BashOperator dalam membuat DAG.

Graph
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1_no1.jpg)

Logs echo
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1no1_logs_echo.jpg)

Logs mkdir-about
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1no1_logs_mkdir-about.jpg)

Logs mkdir-our
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1no1__logs_mkdir-our.jpg)

Logs touch-about
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1no1_logs_touch-about.jpg)

Logs touch-our
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1no1_logs_touch-our.jpg)

logs echoDone
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1no1_logs_echoDone.jpg)

Nomer 2
    a. Task pertama adalah membuat sekumpulan bilangan acak dari 1 sampai 50 dengan jumlah bilangan adalah 25 bilangan.
    b. Task kedua adalah menghitung jumlah dari semua bilangan yang didapatkan dari task pertama.
    c. Task terakhir adalah menentukan apakah jumlah dari semua bilangan merupakan bilangan genap atau bukan. Jika merupakan bilangan genap tampilkan tulisan “Even Sum”. Jika tidak maka tampilkan tulisan “Odd Sum”.
    d. Gunakan X-COM dalam proses pertukaran data antar task.
    e. Gunakan PythonOperator dalam membuat DAG.

Graph
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1_no2.jpg)

Logs generate
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1no2_logs_generate.jpg)

Logs calculate
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1no2_logs_calculate.jpg)

Logs checkEven
![alt text](https://github.com/abdansyakur14002/DE_Abdan-Syakur/blob/main/16.Workflow%20Orchestration%20With%20Airflow/screenshot/prio1no2_logs_checkEven.jpg)

