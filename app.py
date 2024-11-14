import anvil.server
import anvil.app

# Anvil server-side function
@anvil.server.callable
def say_hello(name):
    return f"Hello, {name}!"

# Anvil web app client-side function (HTML interface)
@anvil.app.callable
def main():
    # Simple web app UI that lets the user enter their name
    anvil.app.init_ui("""
      <label>Enter your name:</label>
      <input id="name_input" type="text" />
      <button id="hello_button">Say Hello</button>
      <label id="result"></label>
    """)
    document.getElementById("hello_button").onclick = lambda: say_hello(document.getElementById("name_input").value)
