from enum import Enum

from django.db import models

class MLBTeam(Enum):
    ARI = 'ARI'
    ATL = 'ATL'
    BAL = 'BAL'
    BOS = 'BOS'
    CHC = 'CHC'
    CWS = 'CHI'
    CIN = 'CIN'
    CLE = 'CLE'
    COL = 'COL'
    DET = 'DET'
    FLA = 'FLA'
    HOU = 'HOU'
    KCR = 'KCR'
    LAA = 'LAA'
    LAD = 'LAD'
    MIA = 'MIA'
    MIL = 'MIL'
    MIN = 'MIN'
    NYM = 'NYM'
    NYY = 'NYY'
    OAK = 'OAK'
    PHI = 'PHI'
    PIT = 'PIT'
    SDP = 'SDP'
    SEA = 'SEA'
    SFG = 'SFG'
    STL = 'STL'
    TBR = 'TBR'
    TEX = 'TEX'
    TOR = 'TOR'
    WSH = 'WSH'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]



class Player(models.Model):
    firstname = models.CharField()
    lastname = models.CharField()
    team = models.CharField(choices=MLBTeam.choices(), null=True)
    position = models.CharField(null=True)
    yahoo_id = models.IntegerField(null=True)
    yahoo_status = models.CharField(null=True, default=None)
    curr_hbl_team_id = models.ForeignKey('HblTeam', related_name='players', on_delete=models.SET_NULL, null=True)
    prev_hbl_team_id = models.ForeignKey('HblTeam', related_name='prev_players', on_delete=models.SET_NULL, null=True)

class Prospect(models.Model):
    player_id = models.ForeignKey('Player', related_name='prospects', on_delete=models.CASCADE, unique=True)
    eligible = models.BooleanField(default=True)
