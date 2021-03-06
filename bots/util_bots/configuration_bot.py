import os


class ConfigurationBot:
    def __init__(self):
        print('CONFIGURATION_BOT built and deployed...')

    @staticmethod
    def get_project_pathname():
        cwd = os.getcwd()
        index = cwd.index(r'lotro-bot')
        cpd = ''
        for i in range(len(cwd)):
            if i < index + 9:
                cpd += cwd[i]
            else:
                break
        return cpd

    def generate_is_live_env(self):
        if self.get_project_pathname() == r'C:\Users\Amir Sharapov\Code\bots\lotro-bot':
            return 'False'
        return 'True'

    def generate_config_py(self):
        is_live_env = self.generate_is_live_env()
        f = open(f'{self.get_project_pathname()}\\config.py', 'w')
        nl = '\n'

        f.write(f"PROJECT_DIRECTORY = r'{self.get_project_pathname()}'" + nl)
        f.write(r"IMAGES_DIRECTORY_PATH = PROJECT_DIRECTORY + r'\reference_images'" + nl)
        f.write(r"LOGS_DIRECTORY_PATH = PROJECT_DIRECTORY + r'\logs'" + nl)
        f.write(r"ML_DATA_DIRECTORY_PATH = PROJECT_DIRECTORY + r'\ml_data'" + nl)
        f.write(nl)
        f.write(f"LIVE = {is_live_env}" + nl)
        f.write(nl)
        f.write(r"LOCATION = 'Celondim'" + nl)
        f.close()

    def destroy_config_py(self):
        f = open(f'{self.get_project_pathname()}\\config.py', 'w')
        f.write('')
        f.close()

    def destroy_main_py(self):
        f = open(f'{self.get_project_pathname()}\\main.py', 'w')
        f.write('# Run \'main.py\' to restore this file\n'
                'from bots.util_bots.configuration_bot import ConfigurationBot\n'
                'b = ConfigurationBot()\n'
                'b.restore_default_main_py()\n'
                )
        f.close()

    def restore_default_main_py(self):
        f = open(f'{self.get_project_pathname()}\\main.py', 'w')
        f.write("from bots.util_bots.configuration_bot import ConfigurationBot\n\n"
                "config = ConfigurationBot()\n"
                "config.generate_config_py()\n\n"
                "from bots.reset_bot import ResetBot\n"
                "from bots.game_bots.boss_bots.hobbiton_boss_one import HobbitonBossBot\n\n"
                "reset = ResetBot()\n"
                "boss = HobbitonBossBot()\n\n"
                "reset.count_down(5)\n\n"
                "# boss.do_something_here()\n\n"
                "config.destroy_config_py()\n"
                "# config.destroy_main_py()\n"
                )
        f.close()
