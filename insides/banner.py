"""
"""

from colors import fg, fb, fy, fr, fc, sb

banner = """
{green}

  ____             _     _   ____         __                                _ 
 |  _ \ __ _ _ __ (_) __| | / ___|  __ _ / _| ___  __ _ _   _  __ _ _ __ __| |
 | |_) / _` | '_ \| |/ _` | \___ \ / _` | |_ / _ \/ _` | | | |/ _` | '__/ _` |
 |  _ < (_| | |_) | | (_| |  ___) | (_| |  _|  __/ (_| | |_| | (_| | | | (_| |
 |_| \_\__,_| .__/|_|\__,_| |____/ \__,_|_|  \___|\__, |\__,_|\__,_|_|  \__,_|
            |_|                                   |___/                        
{yellow}Develop by{red}Rapidsafeguard""".format(
    green = fg + sb,
    blue = fb + sb,
    yellow = fy + sb,
    red = fr + sb,
    cyan = fc + sb,
)

# print banner
