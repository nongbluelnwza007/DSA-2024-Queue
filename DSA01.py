class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(f"Queue: {self.items}")
    
    # เมธอด clear เพื่อทำการล้างข้อมูลทั้งหมดในคิว
    def clear(self):
        self.items = []
        print("คิวถูกล้างเรียบร้อยแล้ว")

# สร้าง Queue
q = Queue()

# ทดสอบ 1: ตรวจสอบคิวว่าง
print("คิวว่างหรือไม่:", q.is_empty())  # ควรได้ True

# ทดสอบ 2: เพิ่มข้อมูล
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()  # ควรได้ [1, 2, 3]

# ทดสอบ 3: นำข้อมูลออก
item = q.dequeue()
print("ข้อมูลที่นำออก:", item)  # ควรได้ 1
q.display()  # ควรได้ [2, 3]

# ทดสอบ 4: ดูข้อมูลหน้าคิว
print("ข้อมูลคิวแรก:", q.front())  # ควรได้ 2

# ทดสอบ 5: ล้างคิว
q.clear()  # คิวถูกล้างเรียบร้อยแล้ว
q.display()  # ควรได้ []
 

class Restaurant:
    def __init__(self):
        self.waiting_queue = Queue()
        
    def add_customer(self, name):
        self.waiting_queue.enqueue(name)
        print(f"ลูกค้า {name} เข้าคิวที่ {self.waiting_queue.size()}")
        
    def serve_customer(self):
        if not self.waiting_queue.is_empty():
            customer = self.waiting_queue.dequeue()
            print(f"กำลังเสิร์ฟลูกค้า: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")
            
    def show_queue(self):
        print(f"คิวปัจจุบัน: {self.waiting_queue.items}")
        print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")
        
    def clear_queue(self):
        self.waiting_queue.clear()

# สร้างร้านอาหาร
restaurant = Restaurant()

# เพิ่มลูกค้าเข้าคิว
restaurant.add_customer("อานนท์")
restaurant.add_customer("บุญมี")
restaurant.add_customer("จินดา")

# แสดงสถานะคิว
restaurant.show_queue()

# เสิร์ฟลูกค้า 2 คน
restaurant.serve_customer()
restaurant.serve_customer()

# แสดงสถานะคิวอีกครั้ง
restaurant.show_queue()

# ล้างคิวของร้านอาหาร
restaurant.clear_queue()  # คิวถูกล้างเรียบร้อยแล้ว
restaurant.show_queue()  # ควรได้ []
