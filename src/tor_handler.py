import stem.process
from stem.util import term
  
def connect_to_tor(socks_port):
	print(term.format("Starting Tor:\n", term.Attr.BOLD))

	tor_process = stem.process.launch_tor_with_config(
	  config = {
	    'SocksPort': str(socks_port),
	  },
	  init_msg_handler = print_bootstrap_lines,
	)

	return tor_process

def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))

def change_tor_node(socks_port, tor_process):
	tor_process.kill()
	return connect_to_tor(socks_port)

def disconnect_from_tor(tor_process):
	tor_process.kill()