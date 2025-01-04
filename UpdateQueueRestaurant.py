# UpdateQueueRestaurant.py

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
        if self.is_empty():
            print("คิวว่าง")
        else:
            print(f"Queue: {self.items}")
    
    def peek_last(self):
        if not self.is_empty():
            return self.items[-1]
        return None

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
        
    def peek_last_in_queue(self):
        last_customer = self.waiting_queue.peek_last()
        if last_customer:
            print(f"ลูกค้าคิวสุดท้าย: {last_customer}")
        else:
            print("คิวว่าง")

# สร้างร้านอาหาร
restaurant = Restaurant()

# เพิ่มลูกค้าเข้าคิว
restaurant.add_customer("อานนท์")
restaurant.add_customer("บุญมี")
restaurant.add_customer("จินดา")

# แสดงสถานะคิว
restaurant.show_queue()

# ดูข้อมูลลูกค้าคิวสุดท้าย
restaurant.peek_last_in_queue()  # ควรได้ "จินดา"

# เสิร์ฟลูกค้า 2 คน
restaurant.serve_customer()
restaurant.serve_customer()

# แสดงสถานะคิวอีกครั้ง
restaurant.show_queue()

# เสิร์ฟลูกค้าคนที่ 3 (ที่เหลืออยู่ในคิว)
restaurant.serve_customer()

# แสดงสถานะคิวหลังจากเสิร์ฟลูกค้าทุกคน
restaurant.show_queue()

# เสิร์ฟลูกค้าเมื่อคิวว่าง
restaurant.serve_customer()  # ควรแสดง "ไม่มีลูกค้าในคิว"
