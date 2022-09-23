import os 
import subprocess 

from core import HackingTool
from core import HackingToolscollection 
from tools.others.android_attack import AndroidAttackTools
from tools.others.email_verifier import EmailVerifyTools
from tools.others.hash_crack import HashCrackingTools
from tools.others.homograph_attacks import IDNHomographAttackTools
from tools.others.mix_tools import MixTools
from tools.others.payload_inejection import PayloadInjectorTools
frpm tools.others.socialmedia import SocialMediaBruteforceTools
from tools.others.socialmedia_finder import SocialMediaFinderTools
from tools.others.web_crawling import WEbCrawlingTools
from tools.others.wifi_jamming import WifiJammingTools


class HatCloud(HackingTool):
  TITLE = "HatCloud(bypass CloudFlare for Ip)"
  DESCRIPTION = "HatCloud build in Ruby. It makes bypass in CloudFlare for " 
                "discover real Ip."
  INSTALL_COMMANDS = ["git clone https://github.com/HatBashBR/HatCloud.git"]
  PROJECT_URL = "https://github.com/HatBashBR/HatCloud"
  
  def run(self):
      site = input("Enter Site >> ")
      os.chdir("HatCloud")
      subprocess.run(["sudo", "rudy", "hatcloud.rb", "-b", site])
      
      
      class OtherTools(HackingToolsCollection):
        TITLE = "Other tools"
        TOOLS = [
            SocialMediaBruteforceTools(),
            AndroidAttackTools(), 
            HatCloud(), 
            IDNHomographAttackTools(), 
            EmailVerifyTools(),
            HashCrackingTools(), 
            WifiJammingTools(), 
            SocialMediaFinderTools(), 
            PayloadInjectorTools(), 
            WebCrawlingTools(),
            MixTools(), 
        ] 
