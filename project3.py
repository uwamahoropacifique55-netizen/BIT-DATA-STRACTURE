# Stack Simulation for MoMo
stack = []

# Push operations
stack.append("Step1")
stack.append("Step2")
stack.append("Step3")

# Undo 2 operations (pop 2)
stack.pop()
stack.pop()

# Output the remaining stack
print("Remaining:", stack)
# Stack Simulation for UR Topics
stack = []

# Push topics
stack.append("Topic1")
stack.append("Topic2")
stack.append("Topic3")

# Pop 1 topic
stack.pop()

# View top of stack
print("Current Top:", stack[-1])
# String to reverse
text = "RWANDACODE"

# Step 1: Create stack
stack = []

# Step 2: Push all characters to stack
for char in text:
    stack.append(char)

# Step 3: Pop and build reversed string
reversed_text = ''
while stack:
    reversed_text += stack.pop()

# Output
print("Reversed:", reversed_text)
from collections import deque

scripts = deque()

# Students submit scripts
scripts.append("Student1")
scripts.append("Student2")
scripts.append("Student3")

# Distribute scripts (FIFO)
while scripts:
    print("Returned to:", scripts.popleft())


