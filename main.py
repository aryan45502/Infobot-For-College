import os
import sys

def main():
    print("Starting main loop...")  # Debugging statement

    while True:
        try:
            print("\nChoose an option:")
            print("1. Collect Data")
            print("2. Train Model")
            print("3. Recognize Faces")
            print("4. Delete Image")
            print("5. Exit")
            
            sys.stdout.flush()  # Ensure the prompt is printed immediately

            choice = input("Enter choice: ").strip()
            print(f"Choice entered: {choice}")  # Debugging statement

            if choice == '1':
                try:
                    print("Collect Data selected")  # Debugging statement
                    college_id = int(input("Enter Your College ID: ").strip())
                    name = input("Enter Your Name: ").strip()
                    # Run the script to collect data
                    os.system(f"python CV_Collect.py {college_id} '{name}'")
                except ValueError:
                    print("Please enter a valid integer for College ID.")
            
            elif choice == '2':
                print("Training model...")
                # Run the script to train the model
                os.system("python CV_Train.py")
            
            elif choice == '3':
                print("Recognizing faces...")
                # Run the script to recognize faces
                os.system("python CV_Recognize.py")
            
            elif choice == '4':
                print("Deleting image...")
                # Run the script to delete an image
                os.system("python CV_DeleteByID.py")
            
            elif choice == '5':
                print("Exiting...")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
