from entities.reading_tip import ReadingTip

class App:
    def __init__(self, reading_tip_service, io, tags_service, tip_tags_service, table):
        self.io = io
        self.reading_tip_service = reading_tip_service
        self.tags_service = tags_service
        self.tip_tags_service = tip_tags_service
        self.table = table

        # Initialize (command id -> command handler) map.
        self.commands = {
            0: self.print_all_operations,
            1: self.add_reading_tip,
            2: self.modify_reading_tip,
            3: self.delete_reading_tip,
            4: self.see_all_reading_tips,
            5: self.search_reading_tips_by_title,
            6: self.add_tags_to_existing_reading_tip,
            7: self.see_all_reading_tips_with_tag,
            8: self.add_tag,
            9: self.see_all_tags,
            10: self.mark_as_read,
            11: self.see_all_unread_reading_tips,
            12: self.exit_app,
        }

    def add_reading_tip(self):
        title = self.io.read("Give reading tip title: ")
        if self.validate_title(title):
            link = self.io.read("Give reading tip a link (optional): ")
            author = self.io.read("Give reading tip an author (optional): ")
            description = self.io.read("Give description (optional): ")
            comment = self.io.read("Add comments (optional): ")
            tags = self.io.read("Add tags (optional, separate multiple tags with comma): ")
            status = "Not read yet!"

            tip_id = self.reading_tip_service.create(title, link=link, author=author,
                    description=description, comment=comment, status=status)

            if tip_id is False:
                self.io.write_red("Failed to add a new reading tip!")
            else:
                reading_tip = self.reading_tip_service.get_by_id(tip_id)

                self.add_tags_to_reading_tip(reading_tip, tip_id, tags)

                self.io.write_green("New Reading Tip added!")
        
    def validate_title(self, title):

        title_validation = self.reading_tip_service.validate_title(title)

        if title_validation == 'Empty title':
            self.io.write_red("Reading tip cannot have a empty title!")
            return False

        if title_validation == 'Too many characters':
            self.io.write_red("Reading tip length cannot exceed 200 characters!")
            return False

        return True


    def add_tags_to_existing_reading_tip(self):
        tip_id = self.io.read("To which reading tip you want to tag(s)? Please give id: \n")
        try:
            int(tip_id)
        except:
            self.io.write_red("Please enter id as integer.")
            return
        reading_tip = self.reading_tip_service.get_by_id(tip_id)

        self.add_tags_to_reading_tip(reading_tip, tip_id)

    def add_tags_to_reading_tip(self, reading_tip, tip_id, tags_string=None):
        if reading_tip is None:
            self.io.write_red("Reading tip with id {tip_id} was not found.")
        else:
            if tags_string is None:
                tags_string = self.io.read("Please give tag you want to add to the reading tip. \
                If you want to add multiple tags, separate them with comma: \n")

            tags = tags_string.split(',')
            for tag in tags:
                tag = tag.strip()
                # Add those tags to the database which don't exist already
                if self.tags_service.check_if_tag_exists(tag):
                    pass  
                elif self.tags_service.create_tag(tag):
                    self.io.write_green("New tag created")
                else:
                    self.io.write_red("Failed to create a new tag!")
                    break
                    
                tag_id = self.tags_service.get_tag_id(tag)
                # If tag already added to tip, don't add it again
                if self.tip_tags_service.check_if_tag_added_to_tip(tip_id, tag_id):
                    self.io.write_red(f"Tag {tag} was already added to tip id {tip_id}. \
                        Was not added again.")

                # Add tip-tag pair to TipTags table to the database
                if self.tip_tags_service.add_tag_to_reading_tip(tip_id, tag_id):
                    self.io.write_green(f"Tag {tag} was added successfully to tip id {tip_id}.")
                else:
                    self.io.write_red(f"Failed to add tag {tag} to tip id {tip_id}.")

    def add_tag(self):
        new_tag = self.io.read("Give new tag: ")
        self.tags_service.create_tag(new_tag)
        self.io.write_green("New tag added")

    def mark_as_read(self):
        tip_id = self.io.read("Which reading tip you want to mark as read? Please give id: \n")
        reading_tip = self.reading_tip_service.get_by_id(tip_id)

        if reading_tip is None:
            self.io.write_red(f"Reading tip with id {tip_id} was not found.")
        else:
            self.print_reading_tip(reading_tip)
            new_status = "Already read!"
            reading_tip.status = new_status
            self.reading_tip_service.update_status(reading_tip)
            self.io.write_green("Modification done successfully.")
            self.print_reading_tip(reading_tip)

    def modify_reading_tip(self):
        tip_id = self.io.read("Which reading tip you want to modify? Please give id: \n")
        reading_tip = self.reading_tip_service.get_by_id(tip_id)

        if reading_tip is None:
            self.io.write_red(f"Reading tip with id {tip_id} was not found.")
        else:
            self.print_reading_tip(reading_tip)
            new_title = self.io.read("Enter new title: \n")

            reading_tip.title = new_title
            self.reading_tip_service.update(reading_tip)
            self.io.write_green("Modification done successfully.")

    def delete_reading_tip(self):
        tip_id = self.io.read("Which reading tip you want to delete? Please give id: ")
        reading_tip = self.reading_tip_service.get_by_id(tip_id)
        if reading_tip is None:
            self.io.write_red(f"Reading tip with id {tip_id} was not found.")
        else:
            self.reading_tip_service.delete(tip_id)
            self.io.write_green(f"Deleting a Reading Tip with tip id {tip_id} done successfully.")

    def see_all_reading_tips(self):
        all_tips = self.reading_tip_service.get_all()

        if all_tips:
            self.print_list_of_tips(all_tips)
    
    def see_all_unread_reading_tips(self):
        unread_tips = self.reading_tip_service.get_unread()
        self.io.write("Following reading tips are unread.")
        if unread_tips:
            self.print_list_of_tips(unread_tips)

    def print_list_of_tips(self, tips):
        ids_of_tips = self.reading_tip_service.get_ids(tips)
        tags_of_tips = self.tip_tags_service.get_all_tags_for_multiple_ids(ids_of_tips)

        self.io.write(f"{len(tips)} reading tips found:")

        self.table.create_table(tips, tags_of_tips)

    def see_all_tags(self):
        all_tags = self.tags_service.get_all_tags()
        if all_tags:
            self.print_list_of_tags(all_tags)

    def see_all_reading_tips_with_tag(self):
        self.see_all_tags()
        tag = self.io.read("\nWhich tag you want to filter reading tips with? \n")
        tag = tag.strip()
        if not self.tags_service.check_if_tag_exists(tag):
            self.io.write_red(f"Tag {tag} does not exist.")
            return
        tag_id = self.tags_service.get_tag_id(tag)
        reading_tip_objects = self.tip_tags_service.get_all_reading_tips_with_tag_id(tag_id)
        self.io.write(f"Following reading tips were found with tag {tag}.\n")
        self.print_list_of_tips(reading_tip_objects)

    def search_reading_tips_by_title(self):
        title = self.io.read("Enter title to search for: ")
        tips = self.reading_tip_service.search_by_title(title)
        if tips:
            self.print_list_of_tips(tips)
        else:
            self.io.write_red(f"No reading tips found for title query \"{title}\".")

    def exit_app(self):
        # Raise exit exception.
        # This will stop execution of the app and is not caught by the default exception handler.
        raise SystemExit()

    def print_list_of_tags(self, tags):
        self.io.write(f"{len(tags)} tags found:")
        for tag in tags:
            self.print_tags(tag)

    def print_tags(self, tags):
        self.io.write(tags)

    def print_reading_tip(self, tip: ReadingTip):
        self.io.write(tip.format())

    def print_all_operations(self):
        self.io.write("Choose from the following operations:")
        self.io.write(" 1. Add a Reading Tip")
        self.io.write(" 2. Modify a Reading Tip")
        self.io.write(" 3. Delete a Reading Tip")
        self.io.write(" 4. See all Reading Tips")
        self.io.write(" 5. Search Reading Tips by title")
        self.io.write(" 6. Add tag(s) to a Reading Tip")
        self.io.write(" 7. See all Reading Tips with Tag")
        self.io.write(" 8. Add new tag")
        self.io.write(" 9. See all tags")
        self.io.write(" 10. Mark reading tip as read")
        self.io.write(" 11. See all Unread Reading Tips")
        self.io.write(" 12. Exit software")

    def get_command(self, command):
        command_id = int(command.strip())

        command_handler = self.commands.get(command_id)
        if command_handler:
            command_handler()
        else:
            self.io.write_red(f"No operation found for given number \"{command_id}\"!")
            self.print_all_operations()

    def run(self):
        self.io.write("Welcome to Reading Tip software!")

        self.see_all_unread_reading_tips()
        self.print_all_operations()

        while True:
            try:
                command = self.io.read("Select the operation you want to run (numbers only): \n")
                self.get_command(command)
            except Exception as error:
                self.io.write(str(error))
            except SystemExit:
                break


