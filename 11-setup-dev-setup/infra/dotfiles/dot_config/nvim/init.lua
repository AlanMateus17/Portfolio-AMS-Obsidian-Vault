-- Neovim do setup: lazy.nvim (plugins sob demanda), snacks.nvim (utilitários) e tree-sitter (destaque por AST).
vim.g.mapleader = " "
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.expandtab = true
vim.opt.shiftwidth = 4
vim.opt.clipboard = "unnamedplus"

local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable",
    "https://github.com/folke/lazy.nvim.git", lazypath })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup({
  {
    "folke/snacks.nvim",
    priority = 1000,
    lazy = false,
    opts = { picker = { enabled = true }, explorer = { enabled = true }, lazygit = { enabled = true },
             notifier = { enabled = true }, dashboard = { enabled = true } },
    keys = {
      { "<leader><space>", function() Snacks.picker.smart() end, desc = "Achar arquivo" },
      { "<leader>/", function() Snacks.picker.grep() end, desc = "Buscar texto" },
      { "<leader>e", function() Snacks.explorer() end, desc = "Explorador" },
      { "<leader>gg", function() Snacks.lazygit() end, desc = "lazygit" },
    },
  },
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    opts = { ensure_installed = { "c_sharp", "typescript", "tsx", "go", "rust", "python", "lua", "bash",
                                  "json", "yaml", "toml", "markdown", "sql", "svelte", "astro" },
             highlight = { enable = true } },
    config = function(_, opts) require("nvim-treesitter.configs").setup(opts) end,
  },
}, { checker = { enabled = false } })
