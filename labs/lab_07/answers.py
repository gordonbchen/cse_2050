###############################################################################
# Add your answers to the dictionary below. Possible answers are:             #
#     'bubble'                                                                #
#     'selection'                                                             #
#     'insertion'                                                             #
#     'merge'                                                                 #
#     'quick'                                                                 #
#                                                                             #
# Run this file locally to verify you spelled everything correctly.           #
###############################################################################

answers = {
    "alg_a": "selection",
    "alg_b": "quick",
    "alg_c": "bubble",
    "alg_d": "merge",
    "alg_e": "insertion",
}

# Do not edit anything below this line. This checks that you spelled all answers
# correctly when you run this file.
valid_ans = {"bubble", "selection", "insertion", "merge", "quick"}

for k, v in answers.items():
    if v not in valid_ans:
        raise ValueError(f"Value '{v}' for key '{k}' is not in {valid_ans}")

print("Valid answer! Find out if it's right after the due date.")
