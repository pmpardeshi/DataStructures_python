

class Node:
	def __init__(self,value):
		self.link=None
		self.data=value

	def __str__(self):
		return str(self.data)

class SingleLinkList:
	def __init__(self):
		self.start=None 




	def create_list(self):

		n=int(input('\nEnter number of elements you want to insert: '))
		
		if n :
			for i in range(n):
				data=int(input('\nEnter element: '))
				self.insert_at_end(data)




	def display_list(self):
		if self.start is None:
			print('\nlist is empty')
		else:
			print('\nlist is')
			p=self.start
			while p is not None:
				'''link of last element is none , so if we put loop condition for p.link
				 it will not enter the loop for last element and it will not be printed'''
				print(p.data,end=" ")
				p=p.link
			print()


	def count_nodes(self):
		node_count=0
		p=self.start

		while p is not None:
			node_count+=1
			p=p.link

		print(f'\nnode count is {node_count}')


	def search_nodes(self,key):

		p=self.start
		position=1;

		while p is not None:
			if p.data == key:
				print(f'\n{key} found at position {position}')
				return True
			position+=1
			p=p.link

		print(f'\n{key} not found')
		return False


	def insert_at_begining(self,data):
		temp=Node(data)
		temp.link=self.start
		self.start=temp


	def insert_at_end(self,data):
		temp=Node(data)
		if self.start is None:
			self.start=temp
			return

		p=self.start
		while p.link is not None:
			p=p.link

		p.link=temp


	def insert_after(self,existing_element,data):	
		if self.search_nodes(existing_element):
			p=self.start


			while p.data != existing_element:
				p=p.link

			temp=Node(data)
			temp.link=p.link
			p.link=temp

			print(f'\ninserted {data} after {existing_element}')
			return





	def insert_before(self,existing_element,data):	
		if self.search_nodes(existing_element):
			p=self.start

			if p.data == existing_element:
				self.insert_at_begining(data)
				print(f'\ninserted {data} before {existing_element}')
				return

			while p.link.data != existing_element:
				p=p.link

			temp=Node(data)
			temp.link=p.link
			p.link=temp

			print(f'\ninserted {data} before {existing_element}')
			return




	def insert_at_position(self,position,data):	


			if(position == 1):
				self.insert_at_begining(data)
				return

			i=1
			p=self.start
			while p is not None and i<position-1:
				p=p.link
				i+=1

			if p is None:
				print(f'\ncannot be inserted after position {i}')
				#where p is none is the position immediate after last element beyond which insertion is not possible
				return

			temp=Node(data)
			temp.link=p.link
			p.link=temp

			print(f'\ninserted {data} at {position}')
			return



	def delete_first_node(self):
		if self.start == None:
			print('\nlist is empty')
			return

		self.start=self.start.link


	def delete_last_node(self):
		if self.start == None:
			print('\nlist is empty')
			return

		if self.start.link == None:
			self.start = None
			return

		p=self.start
		while p.link.link != None:
			p=p.link

		print(f'\n removed {p.link}')
		p.link = None



	def delete_element(self,element):

		if self.start.data == element:
			self.delete_first_node(element)
			return

		if self.search_nodes(element):
			p=self.start
			while p.link.data != element:
				p=p.link

			p.link = p.link.link



	def reverse_list(self):
		if self.start is None:
			print('empty list')

		prev_node=None
		next_node=None
		p=self.start

		while p is not None:
			next_node = p.link
			p.link = prev_node
			prev_node = p
			p=next_node

		self.start=prev_node



	def bubble_sort_data_exchange(self):
		if self.start is None:
			print('empty list')

		end=None

		while end is not self.start.link:

			p=self.start

			while p.link is not end:
				q = p.link
				print(q)
				if p.data > q.data:
					p.data,q.data = q.data,p.data
				p=p.link
			end = p
				
			 


link_list=SingleLinkList()
link_list.create_list()

while True:
	print('\n ************')
	print('List Operations')
	print('1 display List')
	print('2 count node')
	print('3 search node')
	print('4 insert at begining')
	print('5 insert at end')
	print('6 insert before element')
	print('7 insert after element')
	print('8 insert at position')
	print('9 delete first element')
	print('10 delete last element')
	print('11 delete particular element')
	print('12 reverse list')
	print('13 bubble sort by exchanging data')
	print('19 quit')

	option = int(input('\nenter your choice: '))

	if(option == 1):
		link_list.display_list()

	elif(option == 2):
		link_list.count_nodes()
	
	elif(option == 3):
		key = int(input('\nenter element to search: '))
		link_list.search_nodes(key)
	
	elif(option == 4):
		data = int(input('\nenter element to insert: '))
		link_list.insert_at_begining(data)
	
	elif(option == 5):
		data = int(input('\nenter element to insert: '))
		link_list.insert_at_end(data)
	
	
	elif(option == 6):
		data = int(input('\nenter element to insert: '))
		existing_element = int(input('\nbefore which element you want to insert it: '))
		link_list.insert_before(existing_element,data)
	
	
	elif(option == 7):
		data = int(input('\nenter element to insert: '))
		existing_element = int(input('\nafter which element you want to insert it: '))
		link_list.insert_after(existing_element,data)
	
	elif(option == 8):
		data = int(input('\nenter element to insert: '))
		position = int(input('\nat which position you want to insert it: '))
		link_list.insert_at_position(position,data)
	
	
	elif(option == 9):
		link_list.delete_first_node()
	
	
	elif(option == 10):
		link_list.delete_last_node()
	
	
	elif(option == 11):
		element = int(input('\nenter element you want to delete: '))
		link_list.delete_element(element)
	
	elif(option == 12):
		link_list.reverse_list()
	
	
	elif(option == 13):
		link_list.bubble_sort_data_exchange()
	
	elif(option == 19):
		print('\n***Ending operations***')
		break

	else:
		print('wrong choice !')
	
