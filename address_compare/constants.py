DIRECTIONS = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'north', 'south', 'east', 'west']
STREET_TYPES = ['alley',
                'aly',
                'annex',
                'anx',
                'arc',
                'arcade',
                'av',
                'ave',
                'avenue',
                'bayoo',
                'bch',
                'beach',
                'bend',
                'bg',
                'bgs',
                'bl',
                'blf',
                'bluff',
                'blvd',
                'bnd',
                'bottom',
                'boulevard',
                'br',
                'branch',
                'brg',
                'bridge',
                'brk',
                'brks',
                'brook',
                'brooks',
                'btm',
                'burg',
                'burgs',
                'byp',
                'bypass',
                'byu',
                'camp',
                'canyon',
                'cape',
                'causeway',
                'center',
                'centers',
                'ci',
                'cir',
                'circle',
                'circles',
                'cirs',
                'cl',
                'clb',
                'clf',
                'clfs',
                'cliff',
                'cliffs',
                'close',
                'club',
                'cmn',
                'common',
                'cor',
                'corner',
                'corners',
                'cors',
                'course',
                'court',
                'courts',
                'cove',
                'coves',
                'cp',
                'cpe',
                'cr',
                'creek',
                'cres',
                'crescent',
                'crest',
                'crk',
                'crossing',
                'crossroad',
                'crse',
                'crst',
                'crt',
                'cswy',
                'ct',
                'ctr',
                'ctrs',
                'cts',
                'curv',
                'curve',
                'cv',
                'cvs',
                'cyn',
                'dale',
                'dam',
                'dgnl',
                'diagonal',
                'divide',
                'dl',
                'dm',
                'dr',
                'drive',
                'drives',
                'drs',
                'dv',
                'est',
                'estate',
                'estates',
                'ests',
                'ewy',
                'expressway',
                'expwy',
                'expy',
                'ext',
                'extension',
                'extensions',
                'exts',
                'falls',
                'ferry',
                'field',
                'fields',
                'flat',
                'flats',
                'fld',
                'flds',
                'fls',
                'flt',
                'flts',
                'ford',
                'fords',
                'forest',
                'forge',
                'forges',
                'fork',
                'forks',
                'fort',
                'frd',
                'frds',
                'freeway',
                'frg',
                'frgs',
                'frk',
                'frks',
                'frst',
                'fry',
                'ft',
                'garden',
                'gardens',
                'gateway',
                'gdn',
                'gdns',
                'glen',
                'glens',
                'gln',
                'glns',
                'grade',
                'grd',
                'green',
                'greens',
                'grn',
                'grns',
                'grove',
                'groves',
                'grv',
                'grvs',
                'gtwy',
                'harbor',
                'harbours',
                'haven',
                'hbr',
                'hbrs',
                'heights',
                'highway',
                'hill',
                'hills',
                'hl',
                'hls',
                'hollow',
                'holw',
                'hts',
                'hvn',
                'hwy',
                'inlet',
                'inlt',
                'is',
                'island',
                'islands',
                'iss',
                'jct',
                'jcts',
                'jr',
                'junction',
                'junctions',
                'junior',
                'k',
                'knl',
                'knls',
                'knoll',
                'knolls',
                'ks',
                'ky',
                'kys',
                'la',
                'lake',
                'lakes',
                'landing',
                'lane',
                'lck',
                'lcks',
                'ldg',
                'lf',
                'lgt',
                'lgts',
                'light',
                'lights',
                'lk',
                'lks',
                'ln',
                'lndg',
                'loaf',
                'lock',
                'locks',
                'lodge',
                'loop',
                'lp',
                'mal',
                'mall',
                'manor',
                'manors',
                'mdw',
                'mdws',
                'meadow',
                'meadows',
                'mill',
                'mills',
                'mission',
                'ml',
                'mls',
                'mnr',
                'mnrs',
                'motorway',
                'mount',
                'mountain',
                'mountains',
                'msn',
                'mt',
                'mtn',
                'mtns',
                'mtwy',
                'nck',
                'neck',
                'opas',
                'orch',
                'orchard',
                'oval',
                'overpass',
                'ovps',
                'park',
                'parkway',
                'passage',
                'pine',
                'pines',
                'pk',
                'pkwy',
                'pky',
                'pl',
                'place',
                'plain',
                'plains',
                'plaza',
                'pln',
                'plns',
                'plz',
                'pne',
                'pnes',
                'point',
                'points',
                'port',
                'ports',
                'pr',
                'prairie',
                'prt',
                'prts',
                'psge',
                'pt',
                'pts',
                'pw',
                'radial',
                'radl',
                'ranch',
                'range',
                'rapid',
                'rapids',
                'rd',
                'rdg',
                'rdgs',
                'rds',
                'rest',
                'rge',
                'ridge',
                'ridges',
                'riv',
                'river',
                'rnch',
                'road',
                'roads',
                'route',
                'rpd',
                'rpds',
                'rst',
                'rte',
                'senior',
                'shl',
                'shls',
                'shoal',
                'shoals',
                'shore',
                'shores',
                'shr',
                'shrs',
                'skwy',
                'skyway',
                'smt',
                'spg',
                'spgs',
                'spring',
                'springs',
                'sq',
                'sqs',
                'square',
                'squares',
                'sr',
                'sta',
                'station',
                'stra',
                'stravenue',
                'stream',
                'streets',
                'strm',
                'sts',
                'summit',
                'te',
                'ter',
                'terr',
                'terrace',
                'tfwy',
                'thfr',
                'thoroughfare',
                'throughway',
                'thruway',
                'thwy',
                'township',
                'tpke',
                'tr',
                'trace',
                'track',
                'trafficway',
                'trail',
                'trak',
                'trce',
                'trfy',
                'trl',
                'trwy',
                'tunl',
                'tunnel',
                'turnpike',
                'twp',
                'un',
                'underpass',
                'union',
                'unions',
                'unp',
                'uns',
                'upas',
                'valley',
                'valleys',
                'via',
                'viaduct',
                'view',
                'views',
                'village',
                'villages',
                'ville',
                'vis',
                'vista',
                'vl',
                'vlg',
                'vlgs',
                'vly',
                'vlys',
                'vw',
                'vws',
                'walkway',
                'way',
                'well',
                'wells',
                'wkwy',
                'wl',
                'wls',
                'wy',
                'xing',
                'xrd']
UNIT_TYPES = ['apt',
              'basement',
              'bsmt',
              'building',
              'bldg',
              'department',
              'dept',
              'floor',
              'fl',
              'front',
              'frnt',
              'hanger',
              'hngr',
              'key',
              'key',
              'lobby',
              'lbby',
              'lot',
              'lot',
              'lower',
              'lowr',
              'office',
              'ofc',
              'penthouse',
              'ph',
              'pier',
              'pier',
              'rear',
              'rear',
              'room',
              'rm',
              'side',
              'side',
              'slip',
              'slip',
              'space',
              'spc',
              'stop',
              'stop',
              'suite',
              'ste',
              'trailer',
              'trlr',
              'unit',
              'upper',
              'uppr']
