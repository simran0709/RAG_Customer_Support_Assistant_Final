def check_confidence(similarity_score):

    if similarity_score < 0.6:
        return True

    return False


def escalate_to_human():

    print("\nEscalating query to human agent...\n")

    response = input("Enter human agent response: ")

    return response