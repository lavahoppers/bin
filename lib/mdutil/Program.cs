using System;
using System.CommandLine;

namespace MarkdownUtilities;

/// <summary>
/// Container for Main function
/// </summary>
class Program
{

    /// <summary>
    /// Main function
    /// </summary>
    /// <param name="args">User provided CLI arguments</param>
    static async Task<int> Main(string[] args)
    {
        var root = new RootCommand("CLI for Markdown parsing");

        // Converting tabular data to a markdown table
        var tableOpt = new Option<FileInfo?>( "--table", 
            "Tabular data to display as a markdown table.");
        root.AddOption(tableOpt);
        root.SetHandler(Tabular.genTable, tableOpt);

        return await root.InvokeAsync(args);
    }
}

