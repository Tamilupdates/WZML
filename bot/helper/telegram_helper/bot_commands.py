from bot import CMD_INDEX
import os
def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command


class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand(f'START_COMMAND', f'start{CMD_INDEX}'), f'srt{CMD_INDEX}'
        self.LeechCommand = getCommand('LEECH_COMMAND', f'leech{CMD_INDEX}'), f'l{CMD_INDEX}'
        self.ZipLeechCommand = getCommand('ZIPLEECH_COMMAND', f'zipleech{CMD_INDEX}'), f'zl{CMD_INDEX}'
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_COMMAND', f'unzipleech{CMD_INDEX}'), f'uzl{CMD_INDEX}'
        self.QbLeechCommand = getCommand('QBLEECH_COMMAND', f'qbleech{CMD_INDEX}'), f'ql{CMD_INDEX}'
        self.QbUnzipLeechCommand = getCommand('QBZIPLEECH_COMMAND', f'qbunzipleech{CMD_INDEX}'), f'quzl{CMD_INDEX}'
        self.QbZipLeechCommand = getCommand('QBUNZIPLEECH_COMMAND', f'qbzipleech{CMD_INDEX}'), f'qzl{CMD_INDEX}'
        self.MirrorCommand = getCommand('MIRROR_COMMAND', f'mirror{CMD_INDEX}'), f'm{CMD_INDEX}'
        self.ZipMirrorCommand = getCommand('ZIP_COMMAND', f'zipmirror{CMD_INDEX}'), f'zm{CMD_INDEX}'
        self.UnzipMirrorCommand = getCommand('UNZIP_COMMAND', f'unzipmirror{CMD_INDEX}'), f'uzm{CMD_INDEX}'
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', f'qbmirror{CMD_INDEX}'), f'qm{CMD_INDEX}'
        self.QbZipMirrorCommand = getCommand('QBZIP_COMMAND', f'qbzipmirror{CMD_INDEX}'), f'qzm{CMD_INDEX}'
        self.QbUnzipMirrorCommand = getCommand('QBUNZIP_COMMAND', f'qbunzipmirror{CMD_INDEX}'), f'quzm{CMD_INDEX}'
        self.WatchCommand =  getCommand('WATCH_COMMAND', f'watch{CMD_INDEX}'), f'w{CMD_INDEX}'
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', f'zipwatch{CMD_INDEX}'), f'zw{CMD_INDEX}'
        self.LeechWatchCommand = getCommand('LEECHWATCH_COMMAND',  f'leechwatch{CMD_INDEX}'), f'lw{CMD_INDEX}'
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_COMMAND', f'leechzipwatch{CMD_INDEX}'), f'lzw{CMD_INDEX}'
        self.CancelMirror = getCommand('CANCEL_COMMAND', f'cancel{CMD_INDEX}')
        self.CancelAllCommand = getCommand('CANCEL_ALL_COMMAND', f'cancelall{CMD_INDEX}'), f'ca{CMD_INDEX}'
        self.ListCommand = getCommand('LIST_COMMAND', f'list{CMD_INDEX}'), f'ls{CMD_INDEX}'
        self.SearchCommand = getCommand('SEARCH_COMMAND', f'search{CMD_INDEX}')
        self.StatusCommand = getCommand('STATUS_COMMAND', f'status{CMD_INDEX}'), f'sts{CMD_INDEX}'
        self.StatsCommand = getCommand('STATS_COMMAND', f'stats{CMD_INDEX}')
        self.AuthorizedUsersCommand = getCommand('USERS_COMMAND', f'kpsusers{CMD_INDEX}'), f'usr{CMD_INDEX}'
        self.PaidUsersCommand = getCommand('PAID_COMMAND', f'paid{CMD_INDEX}'), f'pd{CMD_INDEX}'
        self.AddPaidCommand = getCommand('ADDPAID_COMMAND', f'addpaid{CMD_INDEX}'), f'apd{CMD_INDEX}'
        self.RmPaidCommand = getCommand('RMPAID_COMMAND', f'rmpaid{CMD_INDEX}'), f'rpd{CMD_INDEX}'
        self.PreNameCommand = getCommand('PRENAME_COMMAND', f'prename{CMD_INDEX}'), f'pre{CMD_INDEX}'
        self.CaptionCommand = getCommand('CAPTION_COMMAND', f'caption{CMD_INDEX}'), f'cap{CMD_INDEX}'
        self.UserLogCommand = getCommand('DUMPID_COMMAND', f'dumpid{CMD_INDEX}'), f'dump{CMD_INDEX}'
        self.AuthorizeCommand = getCommand('AUTH_COMMAND', f'kpsauthorize{CMD_INDEX}'), f'au{CMD_INDEX}'
        self.UnAuthorizeCommand = getCommand('UNAUTH_COMMAND', f'kpsunauthorize{CMD_INDEX}'), f'ua{CMD_INDEX}'
        self.AddSudoCommand = getCommand('ADDSUDO_COMMAND', f'addsudo{CMD_INDEX}'), f'asd{CMD_INDEX}'
        self.RmSudoCommand = getCommand('RMSUDO_COMMAND', f'rmsudo{CMD_INDEX}'), f'rsd{CMD_INDEX}'
        self.PingCommand = getCommand('PING_COMMAND', f'ping{CMD_INDEX}')
        self.RestartCommand =  getCommand('RESTART_COMMAND', f'restart{CMD_INDEX}'), f'rst{CMD_INDEX}'
        self.HelpCommand = getCommand('HELP_COMMAND', f'help{CMD_INDEX}')
        self.LogCommand = getCommand('LOG_COMMAND', f'log{CMD_INDEX}')
        self.BtSelectCommand = getCommand('BTSEL_COMMAND', f'btsel{CMD_INDEX}')
        self.SpeedCommand = getCommand('SPEEDTEST_COMMAND', f'speedtest{CMD_INDEX}'), f'spd{CMD_INDEX}'
        self.CloneCommand = getCommand('CLONE_COMMAND', f'clone{CMD_INDEX}'), f'cl{CMD_INDEX}'
        self.CountCommand = getCommand('COUNT_COMMAND', f'count{CMD_INDEX}')
        self.ScrapeCommand = getCommand('SCRAPE_COMMAND', f'scrape{CMD_INDEX}'), f'scr{CMD_INDEX}'
        self.DeleteCommand = getCommand('DELETE_COMMAND', f'del{CMD_INDEX}')
        self.ShellCommand = getCommand('SHELL_COMMAND', f'shell{CMD_INDEX}')
        self.ExecHelpCommand = getCommand('EXEHELP_COMMAND', f'exechelp{CMD_INDEX}')
        self.LeechSetCommand = getCommand('LEECHSET_COMMAND', f'leechset{CMD_INDEX}'), f'lst{CMD_INDEX}'
        self.SetThumbCommand = getCommand('SETTHUMB_COMMAND', f'setthumb{CMD_INDEX}'), f'st{CMD_INDEX}'
        self.MediaInfoCommand = getCommand('MEDIAINFO_COMMAND', f'mediainfo{CMD_INDEX}'), f'mi{CMD_INDEX}'
        self.HashCommand = getCommand('HASH_COMMAND', f'hash{CMD_INDEX}')
        self.RssListCommand = getCommand('RSSLIST_COMMAND', f'rsslist{CMD_INDEX}')
        self.RssGetCommand = getCommand('RSSGET_COMMAND', f'rssget{CMD_INDEX}')
        self.RssSubCommand = getCommand('RSSSUB_COMMAND', f'rsssub{CMD_INDEX}')
        self.RssUnSubCommand = getCommand('RSSUNSUB_COMMAND', f'rssunsub{CMD_INDEX}')
        self.RssSettingsCommand = getCommand('RSSSET_COMMAND', f'rssset{CMD_INDEX}')
        self.WayBackCommand = getCommand('WAYBACK_COMMAND', f'wayback{CMD_INDEX}')
        self.AddleechlogCommand = getCommand('ADDLEECHLOG_CMD', f'addleechlog{CMD_INDEX}'), f'addll{CMD_INDEX}'
        self.RmleechlogCommand = getCommand('RMLEECHLOG_CMD', f'rmleechlog{CMD_INDEX}'), f'rmll{CMD_INDEX}'
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_INDEX}'

BotCommands = _BotCommands()
