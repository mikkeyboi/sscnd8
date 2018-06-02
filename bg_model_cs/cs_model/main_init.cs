using System;

namespace Initialize
{
    class BGnetwork
    {
        static void Main()
        {
            Console.WriteLine("tmax" + Variables.tmax + "dt" + Variables.Instance.dt + "neurons" + Variables.Instance.num_neurons);
            
        }
    }
}

public sealed class Variables
{
    private static readonly Lazy<Variables> lazy = new Lazy<Variables>(() => new Variables());
    public static Variables Instance { get { return lazy.Value; } }

    int tmax = 1000;
    float dt = 0.01f;
    int num_neurons = 10; // # of neurons in each nucleus (TH, STN, GPe, GPi)

    private Variables()
    {
        
    }
}


