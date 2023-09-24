import subprocess

while True:
    # Get user input
    user_input = input("Git Bash > ")

    # Exit the loop if the user enters "exit"
    if user_input.lower() == "exit":
        break

    # Run the Git Bash command
    try:
        result = subprocess.run(
            user_input,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Print the command's standard output and error
        print(result.stdout)
        print(result.stderr)
    except Exception as e:
        print("Error:", e)
