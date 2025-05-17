def navigate_phone_book_menu():
	while True:
		phone_book = input("""
----PHONEBOOK----
1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit 
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
0. Back
""")

		match phone_book:
			case "1": 
				while True:
					search = input("----SEARCH----\nSearch\n0. Back\n")
					match search: 
						case "0" : break
						case _: print("\nInvalid Entry")
			case "2": 
				while True:
					service_nos = input("----SERVICE NOS.----\nService Nos\n0. Back\n")
					match service_nos: 
						case "0" : break
						case _: print("\nInvalid Entry")
			case "3": 
				while True:
					add_name = input("----ADD NAME----\nAdd name\n0. Back\n")
					match add_name: 
						case "0" : break
						case _: print("\nInvalid Entry")
			case "4": 
				while True:
					edit = input("----ERASE----\nErase\n0. Back\n")
					match edit: 
						case "0" : break
						case _: print("\nInvalid Entry")
			case "5": 
				while True:
					edit = input("----EDIT----\nEdit\n0. Back\n")
					match edit: 
						case "0" : break
						case _: print("\nInvalid Entry")
			case "6": 
				while True:
					assign_tone = input("----ASSIGN TONE----\nAssign tone\n0. Back\n")
					match assign_tone: 
						case "0" : break
						case _: print("\nInvalid Entry")
			case "7": 
				while True:
					send_bcard = input("----SEND B'CARD----\nSend b'card\n0. Back\n")
					match send_bcard: 
						case "0" : break
						case _: print("\nInvalid Entry")
			case "8": 
				while True:
					options = input("----OPTIONS----\n1. Type of view\n2. Memory status\n0. Back\n")
					match options: 
						case "1":
							while True:
								type_of_view = input("Type of view\n0. Back\n")
								match type_of_view:
									case "0": break 
									case _: print("\nInvalid Entry")
						case "2":
							while True:
								memory_status = input("Type of view\n0. Back\n")
								match memory_status:
									case "0": break
									case _: print("\nInvalid Entry")
						case "0" : break
						case _: print("\nInvalid Entry")
			case "9": 
				while True:
					speed_dials = input("----SPEED DIALS----\nSpeed dials\n0. Back\n")
					match speed_dials: 
						case "0" : break
						case _: print("\nInvalid Entry")
			case "10": 
				while True:
					voice_tags = input("----VOICE TAGS----\nVoice tags\n0. Back\n")
					match voice_tags: 
						case "0" : break
						case _: print("\nInvalid Entry")
			case "0": break
			case _: print("\nInvalid Entry")
			
def navigate_messages_menu():
	while True:
		messages_menu = input("""
----MESSAGES----
1. Write messages
2. Inbox
3. Outbox
4. Picture Messages
5. Templates
6. Smileys
7. Message settings
8. Info services
9. Voice mailbox number
10. Service command editor
0. Back
""")
	
		match messages_menu:
			case "1": 
				while True:
					write_message = input("----WRITE MESSAGES----\nWrite messages\n0. Back\n")
					match write_message:
						case "0" : break
						case _: print("\nInvalid Entry")
			case "2": 
				while True:
					inbox = input("----INBOX----\nInbox\n0. Back\n")
					match inbox:
						case "0" : break
						case _: print("\nInvalid Entry")
			case "3": 
				while True:
					outbox = input("----OUTBOX----\nOutbox\n0. Back\n")
					match outbox:
						case "0" : break
						case _: print("\nInvalid Entry")
			case "4": 
				while True:
					picture_messages = input("----PICTURE MESSAGES----\nPicture messages\n0. Back\n")
					match picture_messages:
						case "0" : break
						case _: print("\nInvalid Entry")
			case "5": 
				while True:
					templates = input("----TEMPLATE----\nTemplates\n0. Back\n")
					match templates:
						case "0" : break
						case _: print("\nInvalid Entry")
			case "6": 
				while True:
					smileys = input("----SMILEYS----\nSmileys\n0. Back\n")
					match smileys:
						case "0" : break
						case _: print("\nInvalid Entry")
			case "7": 
				while True:
					message_settings = input("----MESSAGE SETTINGS----\n1. Set\n2. Common\n0. Back\n")
					match message_settings:
						case "1":
							while True:
								set1 = input("----SET 1----\n1. Message centre number\n2. Message sent as\n3. Message validity\n0. Back\n")
								match set1:
									case "1":
										while True:
											message_centre_number = input("----MESSAGE CENTRE NUMBER----\nMessage centre number\n0. Back\n")
											match message_centre_number:
												case "0": break
												case _: print("\nInvalid Entry")
									case "2":
										while True:
											messages_sent = input("----MESSAGE SENT----\nMessage sent as\n0. Back\n");
											match messages_sent:
												case "0": break
												case _: print("\nInvalid Entry")
									case "3":
										while True:
											message_validity = input("----MESSAGE VALIDITY----\nMessage validity\n0. Back\n")
											match message_validity:
												case "0": break
												case _: print("\nInvalid Entry")
									case "0": break
									case _: print("\nInvalid Entry")
						case "2":
							while True:
								common = input("----COMMON----\n1. Delivery reports\n2. Reply via same centre\n3. Character support\n0. Back\n")
								match common:
									case "1":
										while True:
											delivery_reports = input("----MESSAGE CENTRE NUMBER----\nMessage centre number\n0. Back\n")
											match delivery_reports:
												case "0": break
												case _: print("\nInvalid Entry")
									case "2":
										while True:
											reply = input("----REPLY VIA SAME CENTRE----\nReply via same centre\n0. Back\n");
											match reply:
												case "0": break
												case _: print("\nInvalid Entry")
									case "3":
										while True:
											character = input("----CHARACTER SUPPORT----\nCharacter support\n0. Back\n")
											match character:
												case "0": break
												case _: print("\nInvalid Entry")
									case "0": break
									case _: print("\nInvalid Entry")
						
						case "0" : break
						case _: print("\nInvalid Entry")
			
			
			case "0": break
			case _: print("\nInvalid Entry")

			
						




def nokia_menu():
	while True:
		menu_choice = input("""
----MENU----
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services 
0. Quit
""")	
		match menu_choice:
			case "1": navigate_phone_book_menu() 
			case "2": navigate_messages_menu() 
			case "3": chat() 
			case "4": call_register() 
			case "5": tones() 
			case "6": settings()
			case "7": call_divert()
			case "8": games() 
			case "9": calculator() 
			case "10": reminders() 
			case "11": clock() 
			case "12": profiles() 
			case "13": sim_services() 
			case "0": break
			case _: print("\nInvalid entry")
	
nokia_menu()

