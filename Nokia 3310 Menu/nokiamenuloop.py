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
			case "8": 
				while True:
					info_service = input("----INFO SERVICE----\nInfo service\n0. Back\n")
					match info_service:
						case "0" : break
						case _: print("\nInvalid Entry")
			case "9": 
				while True:
					voice_mailbox_number = input("----VOICE MAILBOX NUMBER----\nVoice mailbox number\n0. Back\n")
					match voice_mailbox_number:
						case "0" : break
						case _: print("\nInvalid Entry")
			case "10": 
				while True:
					service_command_editor = input("----SERVICE COMMAND EDITOR----\nService command editor\n0. Back\n")
					match service_command_editor:
						case "0" : break
						case _: print("\nInvalid Entry")
			
			case "0": break
			case _: print("\nInvalid Entry")
			
def navigate_chat_menu():
	while True:
		chat = input("\n----CHAT----\nChat\n0. Back\n")
		match chat:
			case "0": break
			case _: print("\nInvalid Entry")
			
def navigate_call_register_menu():
	while True:
		call_register_menu = input("""
----CALL REGISTER----
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid unit
0. Back
""")
		match call_register_menu:
			case "1": 
				while True:
					missed_calls = input("----MISSED CALLS----\nMissed calls\n0. Back\n")
					match missed_calls:
						case "0": break
						case _: print("\nInvalid Entry")
			case "2": 
				while True:
					received_calls = input("----RECEIVED CALLS----\nReceived calls\n0. Back\n")
					match received_calls:
						case "0": break
						case _: print("\nInvalid Entry")
			case "3": 
				while True:
					dialled_numbers = input("----DIALLED NUMBERS----\nDialled numbers\n0. Back\n")
					match dialled_numbers:
						case "0": break
						case _: print("\nInvalid Entry")
			case "4": 
				while True:
					erase_recent_call_lists = input("----ERASE RECENT CALL LISTS----\nErase recent call lists\n0. Back\n")
					match erase_recent_call_lists:
						case "0": break
						case _: print("\nInvalid Entry")
			case "5": 
				while True:
					show_call_duration = input("----SHOW CALL DURATION----\n1. Last call duration\n2. All calls' duration\n3. Received calls' duration\n4. Dialled calls' duration\n5. Clear timers\n0. Back\n")
					match show_call_duration:
						case "1": 
							while True:
								last_call_duration = input("----LAST CALL DURATION----\nLast call duration\n0. Back\n")
								match last_call_duration:
									case "0": break
									case _: print("\nInvalid Entry")
						case "2": 
							while True:
								all_calls_duration = input("----ALL CALLS' DURATION----\nAll calls' duration\n0. Back\n")
								match all_calls_duration:
									case "0": break
									case _: print("\nInvalid Entry")
						case "3": 
							while True:
								received_calls = input("----RECEIVED CALLS----\nReceived calls' duration\n0. Back\n")
								match received_calls:
									case "0": break
									case _: print("\nInvalid Entry")
						case "4": 
							while True:
								dialled_calls = input("----DIALLED CALLS----\nDialled calls' duration\n0. Back\n")
								match dialled_calls:
									case "0": break
									case _: print("\nInvalid Entry")
						case "5": 
							while True:
								clear_timers = input("----CLEAR TIMERS----\nClear timers\n0. Back\n")
								match clear_timers:
									case "0": break
									case _: print("\nInvalid Entry")			
						case "0": break
						case _: print("\nInvalid Entry")
			case "6": 
				while True:
					show_call_costs = input("----SHOW CALL COSTS----\n1. Last call cost\n2. All calls' cost\n3. Clear counters\n0. Back\n")
					match show_call_costs:
						case "1": 
							while True:
								last_call_costs = input("----LAST CALL COSTS----\nLast call cost\n0. Back\n")
								match last_call_costs:
									case "0": break
									case _: print("\nInvalid Entry")
						case "2": 
							while True:
								all_calls_costs = input("----ALL CALLS' COSTS----\nAll calls' cost\n0. Back\n")
								match all_calls_costs:
									case "0": break
									case _: print("\nInvalid Entry")
						case "3": 
							while True:
								clear_counters = input("----CLEAR COUNTERS----\nClear counters\n0. Back\n")
								match clear_counters:
									case "0": break
									case _: print("\nInvalid Entry")
						case "0": break
						case _: print("\nInvalid Entry")
			case "7": 
				while True:
					call_cost_settings = input("----CALL COST SETTINGs----\n1. Call cost limit\n2. Show costs in\n0. Back\n")
					match call_cost_settings:
						case "1": 
							while True:
								call_cost_limit = input("----CALL COST LIMIT----\nCall cost limit\n0. Back\n")
								match call_cost_limit:
									case "0": break
									case _: print("\nInvalid Entry")
						case "2": 
							while True:
								show_costs_in = input("----SHOW COSTS IN----\nShow costs in\n0. Back\n")
								match show_costs_in:
									case "0": break
									case _: print("\nInvalid Entry")
						case "0": break
						case _: print("\nInvalid Entry")
			case "8": 
				while True:
					prepaid_credit = input("----PREPAID CREDIT----\nPrepaid credit\n0. Back\n")
					match prepaid_credit:
						case "0": break
						case _: print("\nInvalid Entry")			
			case "0": break
			case _: print("\nInvalid Entry")

def navigate_tones_menu():
	while True:
		tones_choice = input("""
----TONES----
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
0. Back
""")
		match tones_choice:
			case "1": 
				while True:
					ringing_tone = input("----RINGING TONE----\nRinging tone\n0. Back\n")
					match ringing_tone:
						case "0": break
						case _: print("\nInvalid Entry")
			case "2": 
				while True:
					ringing_volume = input("----RINGING VOLUME----\nRinging volume\n0. Back\n")
					match ringing_volume:
						case "0": break
						case _: print("\nInvalid Entry")
			case "3": 
				while True:
					incoming_alert = input("----INCOMING CALL ALERT----\nIncoming call alert\n0. Back\n")
					match incoming_alert:
						case "0": break
						case _: print("\nInvalid Entry")
			case "4": 
				while True:
					composer = input("----COMPOSER----\nComposer\n0. Back\n")
					match composer:
						case "0": break
						case _: print("\nInvalid Entry")
			case "5": 
				while True:
					message_alert_tone = input("----MESSAGE ALERT TONE\nMessage alert tone\n0. Back\n")
					match message_alert_tone:
						case "0": break
						case _: print("\nInvalid Entry")
			case "6": 
				while True:
					keypad_tones = input("----KEYPAD TONES----\nKeypad tones\n0. Back\n")
					match keypad_tones:
						case "0": break
						case _: print("\nInvalid Entry")
			case "7": 
				while True:
					warning_and_game_tones = input("----WARNING AND GAME TONES----\nWarning and game tones\n0. Back\n")
					match warning_and_game_tones:
						case "0": break
						case _: print("\nInvalid Entry")
			case "8": 
				while True:
					vibrating_alert = input("----VIBRATING ALERT----\nVibrating alert\n0. Back\n")
					match vibrating_alert:
						case "0": break
						case _: print("\nInvalid Entry")
			case "9": 
				while True:
					screen_saver = input("----SCREEN SAVER----\nScreen saver\n0. Back\n")
					match screen_saver:
						case "0": break
						case _: print("\nInvalid Entry")	
			case "0": break
			case _: print("\nInvalid Entry")			
			
def navigate_settings_menu():
	while True:
		settings_choice = input("""
----SETTINGS----
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
0. Back
""")
		match settings_choice:
			case "1":
				while True:
					call_settings_choice = input("----CALL SETTINGS----\n1. Automatic redial\n2. Speed dialing\n3. Call waiting options\n4. Own number sending\n5. Phone line in use\n6. Automatic answer\n0. Back\n")
					match call_settings_choice:
						case "1": 
							while True:
								automatic_redial = input("----AUTOMATIC REDIAL----\nAutomatic redial\n0. Back\n")
								match automatic_redial:
									case "0": break
									case _: print("\nInvalid Entry")
						case "2": 
							while True:
								speed_dialling = input("----SPEED DIALLING----\nSpeed dialling\n0. Back\n")
								match speed_dialling:
									case "0": break
									case _: print("\nInvalid Entry")
						case "3": 
							while True:
								call_waiting_options = input("----CALL WAITING OPTIONS----\nCall waiting options\n0. Back\n")
								match call_waiting_options:
									case "0": break
									case _: print("\nInvalid Entry")
						case "4": 
							while True:
								own_number_sending = input("----OWN NUMBER SENDING----\nOwn number sending\n0. Back\n")
								match own_number_sending:
									case "0": break
									case _: print("\nInvalid Entry")
						case "5": 
							while True:
								phone_line_in_use = input("----PHONE LINE IN USE----\nPhone line in use\n0. Back\n")
								match phone_line_in_use:
									case "0": break
									case _: print("\nInvalid Entry")
						case "6": 
							while True:
								automatic_answer = input("----AUTOMATIC ANSWER----\nAutomatic answer\n0. Back\n")
								match automatic_answer:
									case "0": break
									case _: print("\nInvalid Entry")
						case "0": break
						case _: print("\nInvalid Entry")	
			case "2":
				while True:
					phone_settings_choice = input("----PHONE SETTINGS----\n1. Language\n2. Cell info display\n3. Welcome note\n4. Network selection\n5. Lights\n6. Confirm SIM service actions\n0. Back\n")
					match call_settings_choice:
						case "1": 
							while True:
								language = input("----LANGUAGE----\nLanguage\n0. Back\n")
								match language:
									case "0": break
									case _: print("\nInvalid Entry")
						case "2": 
							while True:
								cell_info_display = input("----CELL INFO DISPLAY----\nCell info display\n0. Back\n")
								match cell_info_display:
									case "0": break
									case _: print("\nInvalid Entry")
						case "3": 
							while True:
								cell_info_display = input("----WELCOME NOTE----\nWelcome note\n0. Back\n")
								match cell_info_display:
									case "0": break
									case _: print("\nInvalid Entry")
						case "4": 
							while True:
								network = input("----NETWORK SELECTION----\nNetwork selection\n0. Back\n")
								match network:
									case "0": break
									case _: print("\nInvalid Entry")
						case "5": 
							while True:
								lights = input("---LIGHTS----\nLights\n0. Back\n")
								match lights:
									case "0": break
									case _: print("\nInvalid Entry")
						case "6": 
							while True:
								sim_service_actions = input("----CONFIRM SIM SERVICE ACTIONS----\nConfirm SIM service actions\n0. Back\n")
								match sim_service_actions:
									case "0": break
									case _: print("\nInvalid Entry")
						case "0": break
						case _: print("\nInvalid Entry")	
			case "3":
				while True:
					security_settings_choice = input("----SECURITY SETTINGS----\n1. PIN code request\n2. Call barring service\n3. Fixed dialling\n4. Closed user group\n5. Phone security\n6. Change access codes\n0. Back\n")
					match security_settings_choice:
						case "1": 
							while True:
								pin_code_request = input("----PIN CODE REQUEST----\nPIN code request\n0. Back\n")
								match language:
									case "0": break
									case _: print("\nInvalid Entry")
						case "2": 
							while True:
								call_barring_service = input("----CALL BARRING SERVICE----\nCall barring service\n0. Back\n")
								match call_barring_service:
									case "0": break
									case _: print("\nInvalid Entry")
						case "3": 
							while True:
								fixed_dialling = input("----FIXED DIALLING----\nFixed dialling\n0. Back\n")
								match fixed_dialling:
									case "0": break
									case _: print("\nInvalid Entry")
						case "4": 
							while True:
								closed_user_goup = input("----CLOSED USER GROUP----\nClosed user group\n0. Back\n")
								match closed_user_goup:
									case "0": break
									case _: print("\nInvalid Entry")
						case "5": 
							while True:
								phone_security = input("----PHONE SECURITY----\nPhone security\n0. Back\n")
								match phone_security:
									case "0": break
									case _: print("\nInvalid Entry")
						case "6": 
							while True:
								change_access_codes = input("----CHANGE ACCESS CODES----\nChange access codes\n0. Back\n")
								match change_access_codes:
									case "0": break
									case _: print("\nInvalid Entry")
						case "0": break
						case _: print("\nInvalid Entry")		
			case "4": 
				while True:
					restore_factory_settings = input("----RESTORE FACTORY SETTINGS----\nRestore factory settings\n0. Back\n")
					match restore_factory_settings:
						case "0": break
						case _:("Invalid Entry")			
			case "0": break
			case _: print("\nInvalid Entry")	
			
def navigate_call_divert_menu():
	while True:
		call_divert = input("\n----CALL DIVERT----\nCall divert\n0. Back\n")
		match call_divert:
			case "0": break
			case _: print("\nInvalid Entry")	
			
def navigate_games_menu():
	while True:
		games = input("\n----GAMES----\nGames\n0. Back\n")
		match games:
			case "0": break
			case _: print("\nInvalid Entry")
			
def navigate_calculator_menu():
	while True:
		calculator = input("\n----CALCULATOR----\nCalculator\n0. Back\n")
		match calculator:
			case "0": break
			case _: print("\nInvalid Entry")
			
def navigate_reminders_menu():
	while True:
		reminders = input("\n----REMINDERS----\nReminders\n0. Back\n")
		match reminders:
			case "0": break
			case _: print("\nInvalid Entry")
			
def navigate_clock_menu():
	while True:
		clock = input("\n----CLOCK----\n1. Alarm clock\n2. Clock settings\n3. Date setting\n4. Stopwatch\n5. Countdown timer\n6. Auto update of date and time\n0. Back\n")
		match clock:
			case "1": 
				while True:
					alarm_clock = input("\n----ALARM CLOCK----\nAlarm clock\n0. Back\n")
					match alarm_clock:
						case "0": break
						case _: print("\nInvalid Entry")
			case "2": 
				while True:
					clock_settings = input("\n----CLOCK SETTINGS----\nClock settings\n0. Back\n")
					match clock_settings:
						case "0": break
						case _: print("\nInvalid Entry")
			case "3": 
				while True:
					date_settings = input("\n----DATE SETTING----\nDate setting\n0. Back\n")
					match date_settings:
						case "0": break
						case _: print("\nInvalid Entry")
			case "4": 
				while True:
					stopwatch = input("\n----STOPWATCH----\nStopwatch\n0. Back\n")
					match stopwatch:
						case "0": break
						case _: print("\nInvalid Entry")
			case "5": 
				while True:
					countdown_timer = input("----COUNTDOWN TIMER----\nCountdown timer\n0. Back\n")
					match countdown_timer:
						case "0": break
						case _: print("\nInvalid Entry")
			case "6": 
				while True:
					auto_update = input("----AUTO UPDATE OF DATE AND TIME----\nAuto update of date and time\n0. Back\n")
					match auto_update:
						case "0": break
						case _: print("\nInvalid Entry")
			case "0": break
			case _: print("\nInvalid Entry")						

def navigate_profiles_menu():
	while True:
		profiles = input("\n----PROFILES----\nProfiles\n0. Back\n")
		match profiles:
			case "0": break
			case _: print("\nInvalid Entry")						

def navigate_sim_services_menu():
	while True:
		sim_services = input("\n----SIM SERVICES----\nSIM services\n0. Back\n")
		match sim_services:
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
0. Back
""")	
		match menu_choice:
			case "1": navigate_phone_book_menu() 
			case "2": navigate_messages_menu() 
			case "3": navigate_chat_menu() 
			case "4": navigate_call_register_menu() 
			case "5": navigate_tones_menu() 
			case "6": navigate_settings_menu()
			case "7": navigate_call_divert_menu()
			case "8": navigate_games_menu() 
			case "9": navigate_calculator_menu() 
			case "10": navigate_reminders_menu() 
			case "11": navigate_clock_menu() 
			case "12": navigate_profiles_menu() 
			case "13": navigate_sim_services_menu() 
			case "0": break
			case _: print("\nInvalid entry")
while True:
	menu = input("""
----NOKIA 3310----
1. Main Menu
0. Quit 
	
""")	
	match menu:
		case "1": nokia_menu()
		case "0": break
		case _: print("\nInvalid entry")

