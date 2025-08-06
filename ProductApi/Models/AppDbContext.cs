using Microsoft.EntityFrameworkCore;

namespace ProductApi.Models
{
    public class AppDbContext : DbContext
    {
        public AppDbContext() { }

        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }
        public DbSet<Product> Products { get; set; }
        public DbSet<Users> Users { get; set; }
    }

}