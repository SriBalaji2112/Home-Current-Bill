# Home-Current-Bill
 Its my first File,
 The electricity bill is needed just to check the final amount and make the payment.



# DeskFrame Project

# DeskFrame: Build Python Applications with XML Frontend

[![PyPI version](https://badge.fury.io/py/deskframe.svg)](https://badge.fury.io/py/deskframe) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/YourUsername/YourRepository/blob/main/LICENSE) ![Tkinter](https://img.shields.io/badge/Tkinter-latest_version-orange) ![CustomTkinter](https://img.shields.io/badge/CustomTkinter-latest_version-darkgreen)

## Introduction

DeskFrame is a Python library that simplifies the process of converting XML code into Python Tkinter applications. This module allows developers to design Tkinter interfaces using XML, providing a dynamic live preview of the Tkinter application as you write XML code.

## Features

### 1. Wide Widget Support

Support for all standard Tkinter and custom Tkinter widgets. Refer to the [documentation](https://github.com/YourUsername/YourRepository/blob/main/docs/widgets.md) for details on available widgets and their usage.

### 2. Live Preview

Once you run the project using `main.py`, all activities run dynamically, providing a simultaneous live preview. Any changes to the XML file are reflected immediately in the live preview window.

### 3. Front in XML

Design the front-end of your Tkinter application using XML.

### 4. Clean Separation

Maintain a clean separation between the front end and back end for better code organization and readability.

### 5. Customizable

Easily customize and fine-tune the generated Tkinter code, including support for custom widgets and layouts.

### 6. User-Friendly Project Structure

Utilize `deskframe.exe` in the site package to create projects effortlessly. Run `deskframe.exe -startProject 'project_name'` in the command prompt. The project includes Python files for backend activities, XML files for layouts, and various resource folders for media, fonts, menus, and values.

### 7. Easy Application Creation

Use the provided `deskframe.exe` tool to streamline project setup, including creating new activities (`python setup.py -createActivity 'activity_name'`), running the DeskFrame server (`python setup.py -server run`), and more.

### 8. Build Executable File

Command: `python setup.py -buildExe`

## Usage

### XML script (Front-end) : `res\layout\activity_main.xml`

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<Layout>
    <TextView
        text="Hello World">
        <Push
            expand="True"/>
    </TextView>
</Layout>
```

### Python Script (Back-end) : `python\MainActivity.py`

```python
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import customtkinter as tk
from deskframe.views.ViewBuilder import Builder

class MainActivity(tk.CTkFrame):
    def __init__(self, master=None, intent=None, **kwargs):
        super().__init__(master, **kwargs)
        self.intent = intent
        self.view = Builder(context="activity_main.xml", _from=self)
        self.onCreate()

    def onCreate(self):
        # Global Variables Declaration
        pass

    # onClick Methods

    # Switch View -> auto created InBuild method, please don't modify
    def Intent(self, view):
        if self.intent:
            self.pack_forget()               # Hide the current window
            self.intent(view)  # Show the destination window
```

### Output :
This script displays a Tkinter window with the centered text "Hello World."

### Create Activity in Project :
#### Command : `python setup.py -createActivity 'activity_name'`

### Run DeskFrame Live Server :
#### Command : `python setup.py -server run`


### Widgets :
# Widget Documentation

Here's a brief overview of each supported widget in DeskFrame, along with a simple description:

```plaintext
+-------------------------+---------------------------------------------------------------+
|          Name           |                      Description                              |
+-------------------------+---------------------------------------------------------------+
| Frame                   | A container for organizing and grouping other widgets.        |
+-------------------------+---------------------------------------------------------------+
| ImageView               | Displays images or icons in your application.                 |
+-------------------------+---------------------------------------------------------------+
| TextView                | Displays text in your application.                            |
+-------------------------+---------------------------------------------------------------+
| Button                  | A clickable button that triggers actions. Supports various    |
|                         | attributes. Refer to the documentation for examples.          |
+-------------------------+---------------------------------------------------------------+
| CheckBox                | A checkable box that allows the user to make a binary choice. |
+-------------------------+---------------------------------------------------------------+
| WebCam                  | Placeholder for webcam-related functionality (customizable).  |
+-------------------------+---------------------------------------------------------------+
| Entry                   | Single-line text entry field.                                 |
+-------------------------+---------------------------------------------------------------+
| VideoView               | Displays video content in your application.                   |
+-------------------------+---------------------------------------------------------------+
| ListBox                 | A list of selectable items.                                   |
+-------------------------+---------------------------------------------------------------+
| MenuButton              | A button that opens a menu when clicked.                      |
+-------------------------+---------------------------------------------------------------+
| Menu                    | A popup menu for providing options and commands.              |
+-------------------------+---------------------------------------------------------------+
| Separator               | A visual separator used to organize layout.                   |
+-------------------------+---------------------------------------------------------------+
| ToolBar                 | A toolbar for quick access to frequently used actions.        |
+-------------------------+---------------------------------------------------------------+
| RadioButton             | A button that allows the user to choose one option from a set.|
+-------------------------+---------------------------------------------------------------+
| Scale                   | A slider that allows the user to select a value from a range. |
+-------------------------+---------------------------------------------------------------+
| LabeledScale            | A labeled slider for selecting a value from a range.          |
+-------------------------+---------------------------------------------------------------+
| Scrollbar               | A scrollbar for navigating content.                           |
+-------------------------+---------------------------------------------------------------+
| NoteBook                | A container for multiple pages with tabs for navigation.      |
+-------------------------+---------------------------------------------------------------+
| SpinBox                 | An input field for selecting numeric values from a range.     |
+-------------------------+---------------------------------------------------------------+
| TreeView                | A hierarchical way to display data in a tree-like structure.  |
+-------------------------+---------------------------------------------------------------+
| PanedFrame              | A container with resizable panes for flexible layout.         |
+-------------------------+---------------------------------------------------------------+
| ComboBox               | A combination of an entry and a dropdown list.                 |
+-------------------------+---------------------------------------------------------------+
| OptionMenu              | A dropdown menu for selecting from a list of options.         |
+-------------------------+---------------------------------------------------------------+
| ProgressBar             | Visualizes the progression of an operation.                   |
+-------------------------+---------------------------------------------------------------+
| ScrollableFrame         | A frame with built-in scrolling capability.                   |
+-------------------------+---------------------------------------------------------------+
| SegmentedButton         | A set of buttons where only one can be selected at a time.    |
+-------------------------+---------------------------------------------------------------+
| Slider                  | Allows the user to select a value from a range using a slider.|
+-------------------------+---------------------------------------------------------------+
| Switch                  | A two-state toggle switch.                                    |
+-------------------------+---------------------------------------------------------------+
| TabView                 | Organizes content into tabs for easy navigation.              |
+-------------------------+---------------------------------------------------------------+
| TextArea                | A multi-line text entry field.                                |
+-------------------------+---------------------------------------------------------------+
| Calendar (DatePicker)   | Allows the user to pick a date from a calendar.               |
+-------------------------+---------------------------------------------------------------+
| TimePicker              | Allows the user to pick a time from a clock interface.        |
+-------------------------+---------------------------------------------------------------+
```
