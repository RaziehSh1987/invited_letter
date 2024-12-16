with open("invited_name.txt") as file1:
    names=file1.readlines( )

with open("starting_letter.txt") as file2:
    letter_content=file2.read()
    for name in names:
        name_strip=name.strip()
        new_letter=letter_content.replace("[name]",name_strip)

        with open(f"letter_for_{name_strip}.txt",mode="w") as complete:
            complete.write(new_letter)
