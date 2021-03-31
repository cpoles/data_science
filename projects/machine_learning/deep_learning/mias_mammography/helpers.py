# MammoScan class 

class MammoScan:
    def __init__(self, scan, sc_info):
        self.scan = scan
        self.sc_info = sc_info

    @property
    def get_x(self):
        return self.sc_info.x
    
    @property
    def get_y(self):
        return self.sc_info.y
        
    @property
    def get_radius(self):
        return self.sc_info.radius
    
    @property
    def get_scan(self):
        return self.scan

    @property
    def get_class(self):
        return self.sc_info['class']

    @property
    def transformations(self):
        return self.__transform

    @property
    def plot(self):
        img = self.get_scan

        # Create a figure. Equal aspect so circles look circular
        fig, ax = plt.subplots(1)

        fig.set_size_inches(12, 10)
        ax.set_aspect('equal')

        # Show the image
        ax.imshow(img)
        ax.set_ylim(bottom=0, top=1024)

        # create a circle to patch on the image
        x = pd.to_numeric(self.get_x)
        y = pd.to_numeric(self.get_y)
        r = pd.to_numeric(self.get_radius)
        circ = Circle((x,1024-y), r, fill=False)
        ax.add_patch(circ)
        print(x, y, r)
    
    # private method
    def _set_x(self, xValue):
        self.sc_info.loc['x'] = xValue
    
    # private method
    def _set_y(self, yValue):
        self.sc_info.y = yValue
    
    # private method
    def _set_radius(self, rValue):
        self.sc_info.radius = rValue
        
    # private method
    def __get_crop_coords(self):
        '''Returns a tuple with x, y and r'''
        # check scan class to decide on how to crop
        if pd.isnull(self.get_radius):
            self._set_radius(48.0)
        if pd.isnull(self.get_x):
            x = float(np.random.randint(500, 513))
            self._set_x(x)
        if pd.isnull(self.get_y):
            y = float(np.random.randint(500, 513))
            self._set_y(y)
            
        return (self.get_x, self.get_y, self.get_radius)
    
    # private method
    def __transform(self):
        '''Creates a dict 
                  with rotated and mirrored versions of self.scan'''
        # create dictionary
        transformations = dict()
        # get crop values
        x, y, r = self.__get_crop_coords()
        # crop and resize scan
        cropped_scan = self.get_scan.crop((x-r, y-r, x+r, y+r))
        resized_scan = cropped_scan.resize((48,48))
        # create rotated images
        for angle in [0, 90, 180, 270]:
            rotated = resized_scan.rotate(angle) # rotated by angle
            mirr_lr = rotated.transpose(Image.FLIP_LEFT_RIGHT)
            mirr_tp = rotated.transpose(Image.FLIP_TOP_BOTTOM)
            transformations[angle] = dict(zip(['rotated', 'mirr_lr', 'mirr_tp'], 
                                         [rotated, mirr_lr, mirr_tp]))

        return transformations


# helper functions

def create_img_dic(path: str) -> dict:
    '''Creates a dictionary with image filenames'''
    paths = Path(path).glob('**/*.pgm')
    img_dic = dict()
    for f_path in sorted(paths):
        # get full filename
        full_fname = f_path.name
        # get filename (no extension)
        filename = f_path.stem
        # create dictionary
        img_dic[filename] = f_path.as_posix()
    
    return img_dic

def get_img_data(filename: str) -> pd.Series:
    '''Returns Series with scan information'''
    try:
        img_data = test_df.loc[filename]
        #print(img_data)
        return img_data
    except KeyError as ie:
        print('Invalid Index')
        

def create_filename(scan_name: str, transf_dic: dict) -> list:
    '''Creates suffix pattern filename for transformed scans'''
    filename = ''
    file_names = list()
    for angle, transfs in transf_dic.items():
        for tf in transfs.keys():
            filename += f'{scan_name}_{angle}_{tf}.pgm'
            #print(filename)
            file_names.append(filename)
            filename = ''
     
    return file_names


def get_transformed_scans(transf_dic: dict):
    '''Returns a list of transformed image scans'''
    scans = list()
    for angle, transfs in transf_dic.items():
        for scan in transfs.values():
            scans.append(scan)
    
    return scans

def save_subsamples(scans_dic: dict(), df: pd.DataFrame):
    '''Save image subsample to the subsamples folder'''
    # define subsamples folder
    folder = 'subsamples'
    # create if not yet
    if not os.path.exists(folder):
        os.mkdir(folder)
    
    # iterate dictionary of filenames
    for scan_name, filename in scans_dic.items():
        
        # create image and scan info objects
        scan = Image.open(filename)
        scan_info = df.loc[scan_name].copy()
        # create the MammoScan object
        m_scan = MammoScan(scan, scan_info)
        # get the transformations
        transf_scans = m_scan.transformations()
        # create filenames
        filenames = create_filename(scan_name, transf_scans)
        # get transformed scans Image objects
        imgs = get_transformed_scans(transf_scans)
        # prepare for saving
        fs_and_is = list(zip(filenames, imgs))
        for filename, image in fs_and_is:
            print(scan_name)
            path = './subsamples/' + filename
            print(path)
            image.save(path)