from pathlib import Path
from typing import List

from ccrestoration import ConfigType, ModelType

projectPATH = Path(__file__).resolve().parent.parent.absolute()


def gen_ts() -> None:
    """
    Automatically generate the list of pretrained models for TypeScript, which is used in the frontend.

    ---

    /**
     * @description: all SR models provided by ccrestoration
     */
    export const modelOptions: any[] = [
      { label: 'RealESRGAN_RealESRGAN_x2plus_2x', value: 'RealESRGAN_RealESRGAN_x2plus_2x.pth' },
      {
        label: 'RealESRGAN_AnimeJaNai_HD_V3_Compact_2x',
        value: 'RealESRGAN_AnimeJaNai_HD_V3_Compact_2x.pth'
      }
    ]

    """

    config_list: List[ConfigType] = []

    # add new sr models here
    all_sr_models = [
        ModelType.RealESRGAN,
        ModelType.DAT,
        ModelType.HAT,
        ModelType.RealCUGAN,
        ModelType.EDSR,
        ModelType.SwinIR,
        ModelType.SCUNet,
        ModelType.SRCNN
    ]

    for cfg in ConfigType:
        for m in all_sr_models:
            if cfg.startswith(m):
                config_list.append(cfg)  # type: ignore

    print(config_list)

    # generate ts file
    ts_file_path = projectPATH / "scripts" / "ModelOptions.ts"

    with open(ts_file_path, "w") as f:
        f.write("/* eslint-disable */\n")
        f.write("/* prettier-ignore */\n")
        f.write("/* tslint:disable */\n")
        f.write("/* This file is automatically generated by Final2x-core */\n")
        f.write("/* Do not modify this file manually */\n")
        f.write("// -----------------------------------------------------------------------------\n\n")

        f.write("/**\n * @description: all SR models provided by ccrestoration\n */\n")
        f.write("export const modelOptions: any[] = [\n")
        for cfg in config_list:
            f.write(f"  {{ label: '{cfg.name}', value: '{cfg.value}' }},\n")
        f.write("]\n")


if __name__ == "__main__":
    gen_ts()
