from typing import Dict, Set


class VoteMenu:
    def __init__(self):
        self.valid_choices: Set[str] = {'v', 'x'}

    def display_menu(self) -> None:
        """Display the vote menu options."""
        print("---------------------\nVOTE MENU\n---------------------")
        print('v. Vote')
        print('x. Exit')

    def get_choice(self) -> str:
        """Get user choice for the vote menu."""
        while True:
            try:
                choice: str = input('Option: ').strip().lower()
                if choice in self.valid_choices:
                    return choice
                else:
                    print("Invalid choice. Please enter 'v' or 'x'.")
            except ValueError:
                print("Invalid input. Please enter 'v' or 'x'.")


class CandidateMenu:
    def __init__(self):
        self.candidates: Dict[int, str] = {1: 'John', 2: 'Jane'}
        self.valid_choices: Set[int] = set(self.candidates.keys())

    def display_menu(self) -> None:
        """Display the candidate menu options."""
        print("---------------------\nCANDIDATE MENU\n---------------------")
        for key, value in self.candidates.items():
            print(f'{key}: {value}')

    def get_choice(self) -> int:
        """Get user choice for the candidate menu."""
        while True:
            try:
                choice: int = int(input('Candidate: '))
                if choice in self.valid_choices:
                    return choice
                else:
                    print('Invalid choice. Please enter 1 or 2.')
            except ValueError:
                print('Invalid input. Please enter 1 or 2.')


class VotingSystem:
    def __init__(self):
        self.candidate_menu: CandidateMenu = CandidateMenu()
        self.vote_menu: VoteMenu = VoteMenu()
        self.votes: Dict[int, int] = {candidate: 0 for candidate in self.candidate_menu.valid_choices}

    def cast_vote(self) -> None:
        """Record a vote for a chosen candidate."""
        try:
            candidate_choice: int = self.candidate_menu.get_choice()
            self.votes[candidate_choice] += 1
            print(f"Voted for {self.candidate_menu.candidates[candidate_choice]}")
        except ValueError:
            print("Invalid input. Please enter a valid candidate choice.")

    def display_results(self) -> None:
        """Display the voting results."""
        print('---------------------')
        total_votes: int = sum(self.votes.values())
        for candidate_num, candidate_name in self.candidate_menu.candidates.items():
            print(f"{candidate_name} - {self.votes[candidate_num]}")
        print(f"Total - {total_votes}")
        print('---------------------')

    def run_voting_system(self) -> None:
        """Run the main voting system loop."""
        while True:
            try:
                self.vote_menu.display_menu()
                vote_choice: str = self.vote_menu.get_choice()

                if vote_choice == 'v':
                    self.cast_vote()
                else:
                    break

            except Exception as e:
                print(f"An error occurred: {e}")

        self.display_results()


def main() -> None:
    """Run the main voting program."""
    try:
        voting_system: VotingSystem = VotingSystem()
        voting_system.run_voting_system()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
