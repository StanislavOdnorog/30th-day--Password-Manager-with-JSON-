from pass_manager import PassManager


class PassManagerMain:
    def __init__(self):
        self.gui = PassManager(title="Password Manager")
        self.gui.configure_objects()
        self.gui.start_loop()


if __name__ == "__main__":
    PassManagerMain()
