#!/usr/bin/env python3

"""
A simple greeting program that demonstrates basic user input and string formatting.

This script prompts the user for their name and prints a personalized greeting message.
Part of the jj-experiment project.
"""


def main():
    """
    Main function that handles the user interaction.

    Prompts the user for their name via standard input and prints a greeting
    using an f-string formatted message.

    Returns:
        None
    """
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
