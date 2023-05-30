using Microsoft.VisualBasic.FileIO;
using System.Text.RegularExpressions;
namespace MarkdownUtilities;

class Tabular
{
    /// <summary>
    /// The delimeter strings that will be used to parse tabular data
    /// </summary>
    /// <value>By default, a singleton list with a comma</value>
    static string[]? delimeters = new string[] {","}; 
    
    /// <summary>
    /// Print a markdown table from a given tabular file
    /// </summary>
    /// <param name="file">The tabular file who's data will be turned into a markdown table</param>
    public static void genTable(FileInfo? file) 
    {
        // file cannot be null
        if (file is null) return;

        // Create reader
        var stream = File.Open(file.FullName, FileMode.Open);
        var parser = new TextFieldParser(stream);
        parser.TextFieldType = FieldType.Delimited;
        parser.SetDelimiters(delimeters);

        // Read each line, line #i...
        for (var i = 0; !parser.EndOfData; i++)
        {
            // only print non-null rows
            var row = parser.ReadFields();
            if (row is null) continue;
            
            // print the rows
            var x = $"| {string.Join(" | ", row)} |";
            Console.WriteLine(x);
            if (i == 0)  // header row
                Console.WriteLine(Regex.Replace(x, "[^,|]", "-"));
        }
    }
}
