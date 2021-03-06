# testing various sagex apis
#
# Run with
#   python test_sageplex.py <media_file>
# Will output data returned from sagex
#
import sys, logging, pprint

from sageplex import plexlog, config, sagex

def sample_mf():
    return {u'Airing': {u'AiringAttributeList': [u'DD5.1', u'New'],
                        u'AiringChannelName': u'KGODT',
                        u'AiringChannelNumber': u'7-1',
                        u'AiringDuration': 3540000,
                        u'AiringEndTime': 1427781600000L,
                        u'AiringID': 3490352,
                        u'AiringPartNumber': 1,
                        u'AiringPremiereFinaleInfo': u'',
                        u'AiringRatings': [u'TVPG'],
                        u'AiringStartTime': 1427778060000L,
                        u'AiringTitle': u'Castle',
                        u'AiringTotalParts': 1,
                        u'Channel': {u'ChannelDescription': u'KGODT (KGO-DT) San Francisco-Oak-San Jose',
                                     u'ChannelLogoCount': 1,
                                     u'ChannelName': u'KGODT',
                                     u'ChannelNetwork': u'ABC Affiliate',
                                     u'ChannelNumber': u'7-1',
                                     u'IsChannelObject': True,
                                     u'IsChannelViewable': True,
                                     u'StationID': 19574},
                        u'ExtraAiringDetails': u'DD5.1',
                        u'IsAiringHDTV': False,
                        u'IsAiringObject': True,
                        u'IsDontLike': False,
                        u'IsFavorite': True,
                        u'IsManualRecord': False,
                        u'IsNotManualOrFavorite': False,
                        u'IsShowFirstRun': True,
                        u'IsShowReRun': False,
                        u'IsWatched': False,
                        u'IsWatchedCompletely': False,
                        u'LatestWatchedTime': 1427778248101L,
                        u'ParentalRating': u'TVPG',
                        u'RealWatchedEndTime': 1429114764171L,
                        u'RealWatchedStartTime': 1429114756572L,
                        u'RecordingName': u'',
                        u'RecordingQuality': u'',
                        u'ScheduleDuration': 3540000,
                        u'ScheduleEndTime': 1427781600000L,
                        u'ScheduleRecordingRecurrence': u'',
                        u'ScheduleStartTime': 1427778060000L,
                        u'Show': {u'IsShowEPGDataUnique': True,
                                  u'IsShowObject': True,
                                  u'OriginalAiringDate': 1427698800000L,
                                  u'PeopleAndCharacterListInShow': [u'Nathan Fillion as Rick Castle',
                                                                    u'Stana Katic as Det. Kate Beckett',
                                                                    u'Susan Sullivan as Martha Rodgers',
                                                                    u'Molly Quinn as Alexis Castle',
                                                                    u'Penny Johnson Jerald as Capt. Victoria Gates',
                                                                    u'Tamala Jones as Lanie Parish',
                                                                    u'Jon Huertas as Det. Javier Esposito',
                                                                    u'Seamus Dever as Det. Kevin Ryan',
                                                                    u'Scott Broderick',
                                                                    u'Nikki DeLoach',
                                                                    u'Don McManus',
                                                                    u'Brian McNamara',
                                                                    u'Meredith Monroe',
                                                                    u'Andrew Marlowe',
                                                                    u'David Amann',
                                                                    u'Rob Bowman',
                                                                    u'Armyan Bernstein',
                                                                    u'Rob Hanning',
                                                                    u'Terri Edda Miller',
                                                                    u'Rob Hanning',
                                                                    u'Kate Woods'],
                                  u'PeopleInShow': u'Nathan Fillion, Stana Katic, Susan Sullivan, Molly Quinn, Penny Johnson Jerald, Tamala Jones, Jon Huertas, Seamus Dever, Scott Broderick, Nikki DeLoach, Don McManus, Brian McNamara, Meredith Monroe, Andrew Marlowe, David Amann, Rob Bowman, Armyan Bernstein, Rob Hanning, Terri Edda Miller, Rob Hanning, Kate Woods',
                                  u'PeopleListInShow': [u'Nathan Fillion',
                                                        u'Stana Katic',
                                                        u'Susan Sullivan',
                                                        u'Molly Quinn',
                                                        u'Penny Johnson Jerald',
                                                        u'Tamala Jones',
                                                        u'Jon Huertas',
                                                        u'Seamus Dever',
                                                        u'Scott Broderick',
                                                        u'Nikki DeLoach',
                                                        u'Don McManus',
                                                        u'Brian McNamara',
                                                        u'Meredith Monroe',
                                                        u'Andrew Marlowe',
                                                        u'David Amann',
                                                        u'Rob Bowman',
                                                        u'Armyan Bernstein',
                                                        u'Rob Hanning',
                                                        u'Terri Edda Miller',
                                                        u'Rob Hanning',
                                                        u'Kate Woods'],
                                  u'RolesInShow': [u'Actor',
                                                   u'Actor',
                                                   u'Actor',
                                                   u'Actor',
                                                   u'Actor',
                                                   u'Actor',
                                                   u'Actor',
                                                   u'Actor',
                                                   u'Guest Star',
                                                   u'Guest Star',
                                                   u'Guest Star',
                                                   u'Guest Star',
                                                   u'Guest Star',
                                                   u'Executive Producer',
                                                   u'Executive Producer',
                                                   u'Executive Producer',
                                                   u'Executive Producer',
                                                   u'Executive Producer',
                                                   u'Executive Producer',
                                                   u'Writer',
                                                   u'Director'],
                                  u'ShowCategoriesList': [u'Crime drama', u'Comedy'],
                                  u'ShowCategoriesString': u'Crime drama / Comedy',
                                  u'ShowCategory': u'Crime drama',
                                  u'ShowDescription': u'Beckett and Castle are faced with a large list of possible suspects when a personal injury attorney known as Richie "The Pitbull" Falco is murdered; a shocking secret deepens the mystery surrounding Richie\'s death.',
                                  u'ShowDuration': 3600000,
                                  u'ShowEpisode': u'Habeas Corpse',
                                  u'ShowEpisodeNumber': 19,
                                  u'ShowExpandedRatings': u'',
                                  u'ShowExternalID': u'EP010855880150',
                                  u'ShowLanguage': u'English',
                                  u'ShowMisc': u'',
                                  u'ShowParentalRating': u'',
                                  u'ShowRated': u'',
                                  u'ShowSeasonNumber': 7,
                                  u'ShowSubCategory': u'Comedy',
                                  u'ShowTitle': u'Castle',
                                  u'ShowYear': u''},
                        u'TrackNumber': 0,
                        u'WatchedDuration': 185096,
                        u'WatchedEndTime': 1427778245101L,
                        u'WatchedStartTime': 1427778060005L},
            u'FileDuration': 3539995,
            u'FileEndTime': 1427781600000L,
            u'FileStartTime': 1427778060005L,
            u'IsBluRay': False,
            u'IsCompleteRecording': True,
            u'IsDVD': False,
            u'IsDVDDrive': False,
            u'IsFileCurrentlyRecording': False,
            u'IsLibraryFile': False,
            u'IsLocalFile': True,
            u'IsMediaFileObject': True,
            u'IsMusicFile': False,
            u'IsPictureFile': False,
            u'IsShowFirstRun': True,
            u'IsShowReRun': False,
            u'IsTVFile': True,
            u'IsThumbnailLoaded': True,
            u'IsVideoFile': True,
            u'MediaFileEncoding': u'Silicondust HDHomeRun Tuner 101A7CC9-1 KGODT',
            u'MediaFileFormatDescription': u'MPEG2-PS[MPEG2-Video 16:9 720p@60fps, Dolby Digital/384Kbps@48kHz 5.1 eng, Dolby Digital/128Kbps@48kHz spa]',
            u'MediaFileID': 3517255,
            u'MediaFileMetadataProperties': {u'Actor': u'Nathan Fillion;Stana Katic;Susan Sullivan;Molly Quinn;Penny Johnson Jerald;Tamala Jones;Jon Huertas;Seamus Dever',
                                             u'Anchor': u'',
                                             u'CC': u'false',
                                             u'ChannelPremiere': u'false',
                                             u'Choreographer': u'',
                                             u'Composer': u'',
                                             u'Contestant': u'',
                                             u'Correspondent': u'',
                                             u'DD51': u'true',
                                             u'Description': u'Beckett and Castle are faced with a large list of possible suspects when a personal injury attorney known as Richie "The Pitbull" Falco is murdered; a shocking secret deepens the mystery surrounding Richie\'s death.',
                                             u'Director': u'Kate Woods',
                                             u'DiscNumber': u'0',
                                             u'Dolby': u'false',
                                             u'Dubbed': u'false',
                                             u'EpisodeName': u'Habeas Corpse',
                                             u'EpisodeNumber': u'19',
                                             u'ExecutiveProducer': u'Andrew Marlowe;David Amann;Rob Bowman;Armyan Bernstein;Rob Hanning;Terri Edda Miller',
                                             u'ExtendedRatings': u'',
                                             u'ExternalID': u'EP010855880150',
                                             u'Genre': u'Crime drama / Comedy',
                                             u'Guest': u'',
                                             u'GuestStar': u'Scott Broderick;Nikki DeLoach;Don McManus;Brian McNamara;Meredith Monroe',
                                             u'GuestVoice': u'',
                                             u'HDTV': u'false',
                                             u'Host': u'',
                                             u'IMDBID': u'tt4488190',
                                             u'Judge': u'',
                                             u'Language': u'English',
                                             u'Letterbox': u'false',
                                             u'Live': u'false',
                                             u'MediaProviderDataID': u'83462',
                                             u'MediaProviderID': u'tvdb',
                                             u'MediaTitle': u'Castle (2009)',
                                             u'MediaType': u'TV',
                                             u'Misc': u'',
                                             u'MusicalGuest': u'',
                                             u'Narrator': u'',
                                             u'New': u'true',
                                             u'OriginalAirDate': u'1427698800000',
                                             u'ParentalRating': u'TVPG',
                                             u'PartNumber': u'0',
                                             u'Premiere': u'false',
                                             u'Producer': u'',
                                             u'Quotes': u'',
                                             u'Rated': u'',
                                             u'RunningTime': u'3600000',
                                             u'SAP': u'false',
                                             u'ScrapedBy': u'Phoenix',
                                             u'ScrapedDate': u'1428473070132',
                                             u'SeasonFinal': u'false',
                                             u'SeasonFinale': u'false',
                                             u'SeasonNumber': u'7',
                                             u'SeasonPremiere': u'false',
                                             u'SeriesFinale': u'false',
                                             u'SeriesInfoID': u'1085588',
                                             u'SeriesPremiere': u'false',
                                             u'Stereo': u'false',
                                             u'Subtitled': u'false',
                                             u'Surround': u'false',
                                             u'TagLine': u'',
                                             u'Taped': u'false',
                                             u'Team': u'',
                                             u'Title': u'Castle',
                                             u'TotalParts': u'0',
                                             u'TrailerUrl': u'',
                                             u'Trivia': u'',
                                             u'UserRating': u'73',
                                             u'Voice': u'',
                                             u'Widescreen': u'false',
                                             u'Writer': u'Rob Hanning',
                                             u'X3D': u'false',
                                             u'Year': u''},
            u'MediaFileRelativePath': u'',
            u'MediaTitle': u'Castle',
            u'NumberOfSegments': 1,
            u'ParentDirectory': u'F:\\SageTV',
            u'SegmentFiles': [u'F:\\SageTV\\Castle-HabeasCorpse-3490352-0.mpg'],
            u'Size': 3634982808L}


def main():
    if len(sys.argv) < 2:
        print 'Usage: <media_file>'
        return

    logging.basicConfig(format='%(asctime)s| %(levelname)-8s| %(message)s',
                        level=logging.DEBUG)
    c = config.Config(sys.platform)
    sageapi = sagex.SageX(c.getSagexHost())

    # test various APIs
    a = sys.argv[1]
    sageapi.log.info('********** getMediaFileForName(%s) **********', a)
    mf = sageapi.getMediaFileForName(a)
    pprint.pprint(mf)
    if not mf:
        return

    a = mf['Airing']['Show']['ShowExternalID']
    sageapi.log.info('********** getShowSeriesInfo(%s) **********', a)
    r = sageapi.getShowSeriesInfo(a)
    pprint.pprint(r)

    a = mf['MediaTitle']
    sageapi.log.info('********** getMediaFilesForShow(%s) **********', a)
    r = sageapi.getMediaFilesForShow(a)
    for f in r:
        sageapi.log.info(f['SegmentFiles'])

    a = mf['MediaFileID']
    sageapi.log.info('********** getMediaFileForID(%s) **********', a)
    r = sageapi.getMediaFileForID(a)
    sageapi.log.info(r['SegmentFiles'])

if __name__ == '__main__':
    main()

# useful stuff
# python falsy values: None/False/0/''/{}
# function implicit return: None
