## ในโฟลเดอร์ Domain
entities.py         ## Graph, Node, Edge (pure Python object)
interfaces.py       ## Abstract class / protocol

## ในโฟลเดอร์ use_cases
find_path.py        ## Dijkstra, BFS logic อยู่ที่นี่
manage_graph.py     ## add/delete node/edge
recommend.py        ## logic แนะนำเส้นทาง
## ในโฟลเดอร์ infrastructure
graph_repository.py ## เก็บข้อมูล (in-memory / file / db)
## ในโฟลเดอร์ presentation
cli.py              ## รับ input จาก user, print ผล
main.py             ## UI UX Display

## ลำดับขั้นตอนการทำงาน
## Important สร้างฟังก์ชั่นสร้าง Graph ให้ add/delete ได้