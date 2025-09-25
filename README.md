# assignment-3
assignment 1 project

- Array Output: Displays the total expenses in a fixed-size array.
- Boolean Output: Indicates whether the average expense exceeds the threshold (true in this case).
- Dictionary Output: Shows the total value of household records based on added items.
- List Output: Displays the current list of expenses before and after an expense is removed.
- String Output: Provides a formatted report summarizing the budget statistics

  **ASSIGNMENT 3 PROJECT 3
  STACK AND QUEUE**


  STACK (LIFO – Last In, First Out)

Think of a stack like a pile of plates. You add (push) on top, and remove (pop or undo) from the top.

LIFO = the last item added is the first to be removed.

🔹 Stack Questions:

MoMo Push ["Step1", "Step2", "Step3"]. Undo 2. Which remains?

Push order: Step1 → Step2 → Step3

Undo 2 (pop 2): Step3 and Step2 removed

✅ Remaining: ["Step1"]

UR pushes ["Topic1", "Topic2", "Topic3"]. Pop 1. Which is top?

Pop 1: Topic3 removed

✅ Top now: Topic2

Challenge: Reverse "RWANDACODE" using stack

Push each letter to stack: R → W → A → N → D → A → C → O → D → E

Pop all letters: E → D → O → C → A → D → N → A → W → R

✅ Reversed: "EDOCADNAWR"

Reflection: Why stack ensures last change first undone?

Because stack removes from the top, the most recent change (last-in) is the first undone (first-out).

Example: Undoing recent steps in a photo editor or calculator.

✅ QUEUE (FIFO – First In, First Out)

Think of a queue like people waiting in line.

First to enter is served first.

FIFO = first added is the first removed.

🔹 Queue Questions:

RRA: 9 clients queue. After 6 served, who is front?

Clients: C1 to C9

After 6 served: C1–C6 gone

✅ Front now: C7

RSSB: 7 clients queue. Who is third?

Clients: C1, C2, C3, C4, C5, C6, C7

✅ Third: C3

Challenge: Queue vs stack for distributing exam scripts. Which is correct?

✅ Queue is correct, because students should receive papers in the order they submitted (FIFO).

Stack would reverse the order (LIFO), which is unfair.

Reflection: Why FIFO ensures fairness in grading?

It processes work in order received, avoiding favoritism or delay.

✅ Ensures equal treatment for all students.
