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
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("คิวว่าง")
        else:
            print(f"Queue: {self.items}")
    
    def peek_first(self):
        if not self.is_empty():
            return self.items[0]
        return None


class BankQueue:
    def __init__(self):
        self.waiting_queue = Queue()
    
    def add_customer(self, name, transaction_type):
        # เพิ่มลูกค้าเข้าไปในคิวพร้อมประเภทธุรกรรม
        self.waiting_queue.enqueue({"name": name, "transaction": transaction_type})
        print(f"ลูกค้า {name} เข้าคิว สำหรับธุรกรรม: {transaction_type}")
        
    def serve_customer(self):
        # เรียกลูกค้าเข้ารับบริการ
        if not self.waiting_queue.is_empty():
            customer = self.waiting_queue.dequeue()
            print(f"กำลังให้บริการลูกค้า: {customer['name']} สำหรับธุรกรรม: {customer['transaction']}")
        else:
            print("ไม่มีลูกค้าในคิว")
    
    def show_waiting_queue(self):
        # แสดงจำนวนลูกค้าในคิว
        print(f"จำนวนลูกค้าที่รอคิว: {self.waiting_queue.size()}")
    
    def estimate_wait_time(self):
        # ประมาณการเวลารอ (สมมติว่าธุรกรรมใช้เวลาเฉลี่ย 5 นาที/คน)
        if not self.waiting_queue.is_empty():
            wait_time = self.waiting_queue.size() * 5  # นาที
            print(f"ประมาณการเวลารอ: {wait_time} นาที")
        else:
            print("ไม่มีลูกค้าในคิว")

# สร้างธนาคาร
bank = BankQueue()

# เพิ่มลูกค้าเข้าคิว
bank.add_customer("กันตพัฒน์", "ฝากเงิน")
bank.add_customer("จอนนี่", "ถอนเงิน")
bank.add_customer("จิรสิน", "ชำระบิล")

# แสดงจำนวนลูกค้าที่รอ
bank.show_waiting_queue()

# แสดงเวลารอประมาณการ
bank.estimate_wait_time()

# เรียกลูกค้าสำหรับธุรกรรม
bank.serve_customer()

# แสดงจำนวนลูกค้าที่รอหลังจากเรียกลูกค้า
bank.show_waiting_queue()

# แสดงเวลารอประมาณการหลังจากเรียกลูกค้า
bank.estimate_wait_time()

# เรียกลูกค้าต่อไป
bank.serve_customer()

# แสดงจำนวนลูกค้าที่รอหลังจากเสิร์ฟ
bank.show_waiting_queue()
bank.estimate_wait_time()

# เรียกลูกค้าทั้งหมด
bank.serve_customer()
bank.show_waiting_queue()
bank.estimate_wait_time()
