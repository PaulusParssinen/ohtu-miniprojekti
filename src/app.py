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
            1: self.add_reading_tip,
            2: self.modify_reading_tip,
            3: self.delete_reading_tip,
            4: self.see_all_reading_tips,
            5: self.search_reading_tips_by_title,
            6: self.add_tags_to_reading_tip,
            7: self.see_all_reading_tips_with_tag,
            8: self.add_tag,
            9: self.see_all_tags,
            10: self.exit_app
        }

    def add_reading_tip(self):
        title = self.io.read("Give reading tip title: ")
        link = self.io.read("Give reading tip a link: ")
        author = self.io.read("Give reading tip an author: ")
        description = self.io.read("Give description: ")
        self.reading_tip_service.create(title, link=link, author=author, description=description)
        self.io.write("New Reading Tip added!")

    def add_tags_to_reading_tip(self):
        tip_id = self.io.read("To which reading tip you want to tag(s)? Please give id: \n")
        try:
            int(tip_id)
        except:
            self.io.write(f"Please enter id as integer.")
            return
        reading_tip = self.reading_tip_service.get_by_id(tip_id)

        if reading_tip is None:
            self.io.write(f"Reading tip with id {tip_id} was not found.")
        else:
            tags_string = self.io.read("Please give tag you want to add to the reading tip. \
                If you want to add multiple tags, separate them with comma: \n")
            tags = tags_string.split(',')
            for tag in tags:
                tag = tag.strip()
                # Add those tags to the database which don't exist already
                if not self.tags_service.check_if_tag_exists(tag):
                    self.tags_service.create_tag(tag)
                tag_id = self.tags_service.get_tag_id(tag)
                # If tag already added to tip, don't add it again
                if self.tip_tags_service.check_if_tag_added_to_tip(tip_id, tag_id):
                    self.io.write(f"Tag {tag} was already added to tip id {tip_id}. \
                        Was not added again.")
                    continue
                # Add tip-tag pair to TipTags table to the database
                if self.tip_tags_service.add_tag_to_reading_tip(tip_id, tag_id):
                    self.io.write(f"Tag {tag} was added successfully to tip id {tip_id}.")
                else:
                    self.io.write(f"Failed to add tag {tag} to tip id {tip_id}.")

    def add_tag(self):
        new_tag = self.io.read("Give new tag: ")
        self.tags_service.create_tag(new_tag)
        self.io.write_green("New tag added")

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
        try:
            tip_id = int(self.io.read("Which reading tip you want to delete? Please give id: "))
        except:
            self.io.write("Invalid reading tip id")
        self.reading_tip_service.delete(tip_id)
        self.io.write_green(f"Deleting a Reading Tip with tip id {tip_id} done successfully.")

    def see_all_reading_tips(self):
        all_tips = self.reading_tip_service.get_all()
        if all_tips:
            self.print_list_of_tips(all_tips)

    def see_all_tags(self):
        all_tags = self.tags_service.get_all_tags()
        if all_tags:
            self.print_list_of_tags(all_tags)

    def see_all_reading_tips_with_tag(self):
        self.see_all_tags()
        tag = self.io.read("\nWhich tag you want to filter reading tips with? \n")
        tag = tag.strip()
        if not self.tags_service.check_if_tag_exists(tag):
            self.io.write(f"Tag {tag} does not exist.")
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
            self.io.write(f"No reading tips found for title query \"{title}\".")

    def exit_app(self):
        # Raise exit exception.
        # This will stop execution of the app and is not caught by the default exception handler.
        raise SystemExit()

    def print_list_of_tips(self, tips):
        self.io.write(f"{len(tips)} reading tips found:")
        #for tip in tips:
        #    self.print_reading_tip(tip)
        self.table.create_table(tips)

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
        self.io.write(" 10. Exit software")

    def run(self):
        self.io.write("Welcome to Reading Tip software!")
        self.print_all_operations()

        while True:
            command = self.io.read("Select the operation you want to run (numbers only): \n")
            try:
                command_id = int(command.strip())

                # Attempt to lookup a matching command handler by the given id
                command_handler = self.commands.get(command_id)

                # If the corresponding command handler was found, call it.
                # If not; write an error message.
                if command_handler:
                    command_handler()
                else:
                    self.io.write(f"No operation found for given number \"{command_id}\"!")
                    self.print_all_operations()

            except Exception as error:
                # This exception handler is a catch-all for all of the command handlers.
                # If the command handler does not have own exception handling,
                # this exception block handles it by simply printing the error to user.
                self.io.write(str(error))
            except SystemExit:
                break
