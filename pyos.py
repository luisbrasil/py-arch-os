import os
import curses
import pycfg
from pyarch import load_binary_into_memory
from pyarch import cpu_t

class os_t:
	def __init__(self, cpu, memory, terminal):
		self.cpu = cpu
		self.memory = memory
		self.terminal = terminal

		self.terminal.enable_curses()

		self.console_str = ""
		self.terminal.console_print("this is the console, type the commands here\n")

	def printk(self, msg):
		self.terminal.kernel_print("kernel: " + msg + "\n")

	def quit(self):
		self.terminal.end() # Finaliza o terminal
		self.cpu.cpu_alive = False # Finaliza o processo da CPU 

	def panic(self, msg):
		self.terminal.end()
		self.terminal.dprint("kernel panic: " + msg)
		self.cpu.cpu_alive = False
		# cpu.cpu_alive = False

	def interrupt_keyboard(self):
		key = self.terminal.get_key_buffer()

		if ((key >= ord('a')) and (key <= ord('z'))) or ((key >= ord('A')) and (key <= ord('Z'))) or ((key >= ord('0')) and (key <= ord('9'))) or (key == ord(' ')) or (key == ord('-')) or (key == ord('_')) or (key == ord('.')):
			self.console_str += chr(key) # Adciona o caracter digitado a string do console;
			self.terminal.console_print("\r" + self.console_str) # Printa a console_str atualizada no console;
		elif key == curses.KEY_BACKSPACE:
			self.console_str = self.console_str[:-1] # Subtrai o ultimo caracter do console_str;
			self.terminal.console_print("\r" + self.console_str) # Printa a console_str atualizada no console;
			return
		elif (key == curses.KEY_ENTER) or (key == ord('\n')):
			self.read_cmd(self.console_str) # Chama a funcao read_cmd que le o comando digitado;
			self.terminal.console_print("\n") # Vai para proxima linha;
			self.console_str = "" # Apaga o console_str
			return

	def interrupt_timer(self):
		self.syscall()

	def read_cmd(self, console_str):
		if console_str == "quit": # Se o comando digitado for "quit"
			self.quit()	# Chama a funcao quit
		if console_str.startswith("run"):
			self.run(console_str)

	def handle_interrupt(self, interrupt):
		if interrupt == pycfg.INTERRUPT_KEYBOARD:
			self.interrupt_keyboard()
		elif interrupt == pycfg.INTERRUPT_TIMER:
			self.interrupt_timer()

	def syscall(self):
		#self.terminal.app_print(msg)
		return

	def run(self, console_str):
		console_array = console_str.split()
		
		if console_array.length != 0:
			printk("teste")

		
