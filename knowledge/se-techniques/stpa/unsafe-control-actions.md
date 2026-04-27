# Unsafe Control Actions — The Four Types

Step 3 of STPA enumerates **Unsafe Control Actions (UCAs)**. For
every control action in the control structure, four questions are
asked. Each question corresponds to one UCA type.

## The four UCA types

1. **Not providing.** *What happens if this control action is not
   issued when it should be?*
   Example: parliament does not withdraw confidence from an
   executive that has acted unconstitutionally.

2. **Providing.** *What happens if this control action is issued
   when it should not be, or the wrong action is issued?*
   Example: a regulator grants a licence to an applicant that
   does not meet the statutory conditions.

3. **Too early, too late, or wrong order.** *What happens if the
   timing or sequence of the control action is wrong?*
   Example: a budget is approved after the fiscal year has
   already begun; an indictment is issued before evidence has been
   gathered.

4. **Applied too long, or stopped too soon.** *What happens if
   the duration of the control action is wrong?*
   Example: an emergency power is kept in force after the
   emergency has ended; a subsidy is withdrawn before the policy
   goal has been achieved.

## How to use the four types

For every control action in the Step 2 diagram, produce a row of
the UCA table:

| Control Action | Not providing | Providing | Timing | Duration |
|----------------|---------------|-----------|--------|----------|

Each cell is either empty (the action is safe in that type) or a
specific UCA statement referring to a Step 1 hazard. Empty cells
are as important as filled ones: they represent an explicit
judgement that the timing or providing case is not hazardous.

## Why four types and not more

The four types are exhaustive in the sense that any way a
single-action control loop can fail reduces to one of these four
categories. More complex failures (wrong sequence across multiple
actions, coordination failures between controllers) are still
found by applying the four types to each individual action and
then looking at the interactions in Step 4.

## Rung-mismatch UCA modes (social-systems extension)

In social systems a control action may be issued at the right
time, in the right form, and against a real hazard, yet still
fail because the **justificatory rung** of the action does not
match the rung at which the receiver operates. Three rung-mismatch
UCA modes cut across the four types above:

- **UCA-R1 — Over-rung command.** Control action issued at a rung
  the receiver cannot decode (rung 4 evidence delivered to a
  rung-1 audience). Fails *silently*; the controller may believe
  it was obeyed.
- **UCA-R2 — Under-rung command.** Control action issued at a rung
  the receiver rejects as illegitimate (rung 1 authority delivered
  to a rung-4 audience). Fails *noisily* and erodes the
  controller's standing.
- **UCA-R3 — Asymmetric loop.** Control action and feedback on the
  same loop operate at different rungs, so the controller cannot
  register the corrective signal even when it arrives.

Full treatment in
`../justification-rungs/application-to-stpa.md`. UCA-R3 is the most
common rung-mismatch UCA in hierarchical social systems and the
hardest to remedy.

## Reading the UCA table as a design checklist

The UCA table is not just a hazard list; it is a design
checklist. Every non-empty cell is a place where the control
structure currently permits a hazardous state. The job of Step 4
is to find out *why* it permits it, and the job of the remedy
catalogue is to say *what to change* so it no longer does.
