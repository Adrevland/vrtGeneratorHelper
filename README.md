<h1>Python scripts to help generate .vrt files</h1>

<h2>Generator.py creates a new file that list files to be used in the .vrt generator</h2>
<h3>Example how to use Generator.py</h3>
Generator.py {RootDir} {Output file} {filetype}

- python Generator.py d:/Terrain d:/TerrainList.txt .dt1

Example creates a file on d: with the name TerrainList.txt, The file includes location to all .dt1 files in all subdirs of d:/Terrain, each filelocation is line seperated for the gdalbuildvrt to understand
